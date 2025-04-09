consumer=kafka-consumer:latest

build:
	docker build --no-cache -t $(consumer) .

test:
	docker run --rm -it $(consumer)

upload:
	minikube image load --overwrite $(consumer)

all: build upload

clean:
	minikube image rm docker.io/library/$(consumer)

