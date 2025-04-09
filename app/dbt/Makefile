dbtRunner=dbt-runner:latest

build:
	docker build --platform linux/amd64 --no-cache -t $(dbtRunner) .

test:
	docker run --rm -it $(dbtRunner)

upload:
	minikube image load --overwrite $(dbtRunner)

all: build upload

clean:
	minikube image rm docker.io/library/$(dbtRunner)
