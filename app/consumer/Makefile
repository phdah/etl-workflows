consumer=kafka-consumer:latest

build:
	docker build --no-cache -t $(consumer) .

test:
	docker run --rm -it $(consumer)

upload:
	@echo "Sometimes the image is not recreated, then call:"
	@echo "minikube ssh"
	@echo "docker rmi kafka-consumer:latest"
	@echo "exit"
	minikube image load --overwrite $(consumer)

all: build upload
