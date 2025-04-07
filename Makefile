run-producer:
	python ./app/producer/kafka_producer.py ./sample-superstore.xlsx

build-consumer:
	make -C ./app/consumer/ all

consumer: build-consumer
	kubectl apply -f ./app/consumer/kafka-consumer-workflow.yaml -n argo-workflow

set-docker-env:
	eval $(minikube -p minikube docker-env)

