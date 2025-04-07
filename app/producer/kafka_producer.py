from typing import Dict
import time
import json

from kafka import KafkaProducer


def kafkaSender(topic: str, config: Dict[str, str], events: int) -> None:
    """
    Arguments:
        topic (str): target kafka topic to which the message is being sent to
        bootstrapServers (str): the 'host[:port]' for the API call, defaults to 'localhost:9092'
    """
    producer = KafkaProducer(**config)

    start_time = time.time()
    for i in range(events):
        message = json.dumps({"message_id": i})
        producer.send(topic, value=message)
        producer.flush()
    end_time = time.time()
    executionTime: float = end_time - start_time

    if events:
        print(
            f"Function took {executionTime} seconds to execute, for {events} events, with a mean of {events/executionTime} events/s"
        )
    else:
        print(f"Function ran for {executionTime} seconds")


kafkaTopic = "my-topic"

config = {
    "bootstrap_servers": "127.0.0.1:9094",
    "value_serializer": lambda x: x.encode("utf-8"),
}

kafkaSender(kafkaTopic, config, 10)
