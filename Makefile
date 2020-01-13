.PHONY = build-test run-test debug-test

build-test:
	docker build \
		--file Dockerfile.test \
		--tag flask_test_image \
		.

run-test: build-test
	docker run flask_test_image

debug-test: build-test
	docker run -it --entrypoint /bin/bash flask_test_image
