.PHONY = build-test run-test debug-test
IMAGE_NAME=flask_test

build-test:
	docker build \
		--file Dockerfile.test \
		--tag $(IMAGE_NAME) \
		.

run-test: build-test
	docker run $(IMAGE_NAME)

debug-test: build-test
	docker run -it --entrypoint /bin/bash $(IMAGE_NAME)
