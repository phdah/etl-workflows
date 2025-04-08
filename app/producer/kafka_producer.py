from typing import Dict
import time
import json
import sys
import pandas as pd

from kafka import KafkaProducer


def kafkaSender(topic: str, config: Dict[str, str], file_path: str) -> None:
    """
    Arguments:
        topic (str): target kafka topic to which the message is being sent to
        config (dict): Configuration for the Kafka consumer.
        file_path (str): Path to the xlsx file to be loaded.
    """
    producer = KafkaProducer(**config)

    # Read only the first sheet
    df = pd.read_excel(file_path, sheet_name=0)

    start_time = time.time()
    for idx, row in df.iterrows():
        record = {
            k: (
                v.isoformat()
                if isinstance(v, pd.Timestamp) and not pd.isna(v)
                else None
                if pd.isna(v)
                else v
            )
            for k, v in row.to_dict().items()
        }
        message = json.dumps(record)
        producer.send(topic, value=message)
        producer.flush()
        print(f"Sent row {idx}")
        time.sleep(0.0046)
    end_time = time.time()
    executionTime: float = end_time - start_time

    print(f"Function ran for {executionTime} seconds")


kafkaTopic = "my-topic"

config = {
    "bootstrap_servers": "127.0.0.1:9094",
    "value_serializer": lambda x: x.encode("utf-8"),
}

kafkaSender(kafkaTopic, config, sys.argv[1])
