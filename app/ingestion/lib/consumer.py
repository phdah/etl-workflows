from kafka import KafkaConsumer
import json

def kafkaConsumer(topic: str, config: dict) -> None:
    """
    Consumes messages from a specified Kafka topic.

    Arguments:
        topic (str): The Kafka topic to consume messages from.
        config (dict): Configuration for the Kafka consumer.
    """
    consumer = KafkaConsumer(
        topic,
        **config
    )

    for message in consumer:
        # Assuming the message value is in JSON format
        data = json.loads(message.value.decode('utf-8'))
        print(f"Received message: {data}")

