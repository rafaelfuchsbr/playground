GIT_SHA1 = $(shell git rev-parse --verify HEAD)
IMAGES_TAG = ${shell git describe --exact-match 2> /dev/null || echo 'latest'}

IMAGE_DIRS = $(wildcard services/* bases/*)

# All targets are `.PHONY` ie allways need to be rebuilt
.PHONY: all ${IMAGE_DIRS}

# Build all images
all: ${IMAGE_DIRS}

# Build and tag a single image
${IMAGE_DIRS}:
	$(eval IMAGE_NAME := $(word 2,$(subst /, ,$@)))
	echo "building $(IMAGE_NAME)"
	echo docker build -t monorepo/${IMAGE_NAME}:$(cat $(IMAGE_NAME)/VERSION ) -t monorepo/${IMAGE_NAME}:${IMAGES_TAG} -t monorepo/${IMAGE_NAME}:latest --build-arg TAG=${IMAGES_TAG} --build-arg GIT_SHA1=${GIT_SHA1} $@


# Specify dependencies between images
bases/cool-node: bases/alpine
services/go-image: bases/alpine
services/my-node-service: bases/cool-node
services/my-rust-service: bases/fancy-rust
services/my-python-service: bases/nice-python
