.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help text
	$(info oneshot-import)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: setup
setup: setup-api setup-frontend ## Setup the project
	echo "Setup finished."


.PHONY: setup-api
setup-api:  ## Setup the api
	cd backend/api && pipenv install --dev

export WEBROOT_PATH = ../../_local_webroot
export LOGGING_LEVEL = "DEBUG"
.PHONY: start-api
start-api:  ## Start the api
	cd backend/api && pipenv run python src/main.py

.PHONY: setup-frontend
setup-frontend:  ## Setup the frontend
	cd frontend && npm install --dev

.PHONY: start-frontend
start-frontend:  ## Start the frontend
	cd frontend && ionic serve

.PHONY: compile-frontend
compile-frontend:  ## Compile the frontend
	cd frontend && npm run build

.PHONY: build-docker-image-no-compile
build-docker-image-no-compile: ## Build the docker image with nginx, python api server and the compiled frontend in it. Skip compilation of the frontend (build outside of the devcontainer).
	docker build -t oneshot-web .

.PHONY: build-docker-image
build-docker-image: compile-frontend build-docker-image-no-compile ## Build the docker image with nginx, python api server and the compiled frontend in it
	echo "Done."


.PHONY: ci-release-docker-image
ci-release-docker-image:  ## Setup build-docker-image
	#todo release to docker hub


.PHONY: start-docker-image
start-docker-image: build-docker-image-no-compile  ## Start the docker image without a db. Make sure that the frontend was compiled before.
	mkdir -p local_volume/api
	docker run --rm -it --name os-web --volume=./local_volume/api/:/srv/oneshot -p 80:8080 oneshot-web /bin/bash

.PHONY: start-compose-stack
start-compose-stack: build-docker-image-no-compile  ## Start the application with docker compose. Make sure that the frontend was compiled before.
	mkdir -p local_volume/api
	mkdir -p local_volume/api
	docker compose up -d
