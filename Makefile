batch-upload:
	./load_data.sh

run-producer: batch-upload
	python ./app/producer/kafka_producer.py ./sample-superstore.xlsx

build-consumer: set-docker-env
	make -C ./app/consumer/ all

build-dbt-runner: set-docker-env
	make -C ./app/dbt/ all

consumer: build-consumer
	kubectl apply -f ./app/consumer/kafka-consumer-workflow.yaml -n argo-workflow

dbt-runner: build-dbt-runner
	kubectl apply -f ./app/dbt/dbt-workflow.yaml -n argo-workflow

set-docker-env:
	eval $(minikube -p minikube docker-env)

