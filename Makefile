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

.PHONY: start-api
start-api:  ## Start the api
	cd backend/api && LOGGING_LEVEL=DEBUG STAGE=dev pipenv run python src/main.py

.PHONY: start-admintools
start-admintools:  ## Start the admintools
	cd backend/api && pipenv run python admintools/main.py


.PHONY: setup-frontend
setup-frontend:  ## Setup the frontend
	cd frontend && npm install --include=dev

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
build-docker-image: compile-frontend build-docker-image-no-compile ## Build the docker image with nginx, the python api server and the compiled frontend in it.
	echo "Done."

.PHONY: start-docker-image-bash
start-docker-image-bash: build-docker-image-no-compile  ## Start the docker but run bash instead. Inside the container, run the api with `pipenv run python src/main.py`, nginx with `nginx -g 'daemon off;'` or both with `/usr/bin/supervisor`. Make sure that the frontend was compiled before.
	mkdir -p ./_local_volume/api
	docker run --rm -it --name os-web -e TZ="Europe/Berlin" -e HOST_URL="localhost:8080" -e STAGE="qa" --volume=./_local_volume/api/:/srv/oneshot -p 8080:80 --network=os-web-db oneshot-web /bin/bash

.PHONY: start-docker-image
start-docker-image: build-docker-image-no-compile  ## Start the docker image. Make sure that the frontend was compiled before.
	mkdir -p ./_local_volume/api
	docker run --rm --name os-web -e TZ="Europe/Berlin" -e HOST_URL="localhost:8080" -e STAGE="qa" --volume=./_local_volume/api/:/srv/oneshot -p 8080:80 --network=os-web-db oneshot-web

.PHONY: container-attach-bash
container-attach-bash:  ## Attach a shell to the docker container.
	docker exec -it os-web /bin/bash

.PHONY: start-docker-postgres
start-docker-postgres:  ## Start the docker image from Docker Hub.
	docker run --rm --name os-web-db -e POSTGRES_PASSWORD="password" --volume=./_local_volume/db/:/var/lib/postgresql/data/ -p 5432:15432 --network=os-web-db postgres:latest

.PHONY: ping-postgres
ping-postgres:  ## Ping the postgres-container from the devcontainer.
	ping os-web-db

.PHONY: start-docker-compose-stack
start-docker-compose-stack: build-docker-image-no-compile  ## Start the docker image and database with docker compose. Make sure that the frontend was compiled before.
	mkdir -p ./_compose_volume
	docker compose up


.PHONY: pull-and-start-docker-image
pull-and-start-docker-image:  ## Start the docker image from Docker Hub.
	# mkdir -p ./_local_volume/api
	docker run --rm -e TZ="Europe/Berlin" -e HOST_URL="localhost:8080" -e STAGE="prod" -p 8080:80 ptrlx/oneshot-web # --volume=./_local_volume/api/:/srv/oneshot 
