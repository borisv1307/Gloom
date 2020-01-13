.PHONY = build-test-image run-test-image debug-test-image

build-test-image:
	docker build \
		--file Dockerfile.test \
		--tag flask_test_image \
		.

run-test-image: build-test-image
	docker run flask_test_image

debug-test-image: build-test-image
	docker run -it --entrypoint /bin/bash flask_test_image
