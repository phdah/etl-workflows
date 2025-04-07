run-producer:
	python ./app/producer/kafka_producer.py

build-consumer:
	make -C ./app/consumer/ all

consumer: build-consumer
	kubectl apply -f ./app/consumer/kafka-consumer-workflow.yaml -n argo-workflow
