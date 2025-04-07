from kafka import KafkaConsumer
import json
import psycopg2


def kafkaConsumer(topic: str, config: dict, postgres: dict) -> None:
    """
    Consumes messages from a specified Kafka topic.

    Arguments:
        topic (str): The Kafka topic to consume messages from.
        config (dict): Configuration for the Kafka consumer.
        postgres (dict): Configuration for the postgres target.
    """
    consumer = KafkaConsumer(topic, **config)

    conn = psycopg2.connect(**postgres)
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        create table if not exists orders (
            id serial primary key,
            created_at timestamp default current_timestamp,
            updated_at timestamp default current_timestamp,
            content text not null
        );
    """)
    conn.commit()

    # Insert query with conflict handling
    insert_query = """
        insert into orders (content)
        values (%s);
    """

    for message in consumer:
        data = json.loads(message.value.decode("utf-8"))
        print(f"Received message: {data}")

        # Convert dict to JSON string for insertion
        cur.execute(insert_query, (json.dumps(data),))
        conn.commit()

    cur.close()
    conn.close()


kafkaTopic = "my-topic"

config = {
    "bootstrap_servers": "my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092",
}

postgres = {
    "dbname": "mydatabase",
    "user": "myuser",
    "password": "mypassword",
    "host": "postgres.postgres.svc.cluster.local",
    "port": "5432",
}

print(f"Consuming from topic {kafkaTopic}")
kafkaConsumer(kafkaTopic, config, postgres)
