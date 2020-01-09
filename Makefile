.PHONY = build-test-image run-test-image

build-test-image:
	docker build \
		--file Dockerfile.test \
		--tag flask_test_image \
		.

run-test-image: build-test-image
	docker run flask_test_image
