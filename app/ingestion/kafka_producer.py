from app.ingestion.lib.producer import kafkaSender

kafkaTopic = "my-topic"

config = {
    "bootstrap_servers": "127.0.0.1:9094",
    "value_serializer": lambda x: x.encode("utf-8"),
}

kafkaSender(kafkaTopic, config, 10)
