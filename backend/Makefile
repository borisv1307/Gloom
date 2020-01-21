.PHONY = build run debug
IMAGE_NAME=flask_test

build:
	docker build \
		--file Dockerfile.test \
		--tag $(IMAGE_NAME) \
		.

run: build
	docker run $(IMAGE_NAME)

debug: build
	docker run -it --entrypoint /bin/bash $(IMAGE_NAME)
