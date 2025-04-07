from app.ingestion.lib.consumer import kafkaConsumer

kafkaTopic = "my-topic"

config = {
    "bootstrap_servers": "127.0.0.1:9094",
}

kafkaConsumer(kafkaTopic, config)

