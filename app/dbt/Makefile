consumer=dbt-runner:latest

build:
	docker build --platform linux/amd64 --no-cache -t $(consumer) .

test:
	docker run --rm -it $(consumer)

upload:
	@echo "Sometimes the image is not recreated, then call:"
	@echo "minikube ssh"
	@echo "docker rmi dbt-runner:latest"
	@echo "exit"
	minikube image load --overwrite $(consumer)

all: build upload
