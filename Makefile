.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help text
	$(info oneshot-import)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: setup
setup: setup-api generate-prisma-client setup-frontend  ## Setup the project
	echo "Setup finished."


.PHONY: setup-api
setup-api:  ## Setup the api
	cd backend/api && pipenv install --dev

.PHONY: generate-prisma-client
generate-prisma-client:  ## Generate the prisma client for the connection between api and database.
	cd backend/api && pipenv run prisma generate

.PHONY: dev-database-prisma-setup
dev-database-prisma-setup:  ## Migrate the database to the current schema.prisma.
	cd backend/api && DATABASE_URL="postgresql://postgres:password@os-web-db:5432/osweb?schema=public" pipenv run prisma db push

.PHONY: start-api
start-api:  ## Start the api
	cd backend/api && STAGE=dev pipenv run python src/main.py

.PHONY: start-admintools
start-admintools:  ## Start the admintools
	cd backend/api && STAGE=dev pipenv run python admintools/main.py


.PHONY: setup-frontend
setup-frontend:  ## Setup the frontend
	cd frontend && npm install --include=dev

.PHONY: start-frontend
start-frontend:  ## Start the frontend
	cd frontend && npx vite --host=127.0.0.1

.PHONY: compile-frontend
compile-frontend:  ## Compile the frontend
	cd frontend && VITE_DEPLOYMENT_MODE=SAME_HOST npm run build

.PHONY: gen-api-client
gen-api-client:  ## Generate api client for frontend
	cd frontend && npm run gen-api-client && npx prettier --write src/_generated


.PHONY: build-docker-image-no-compile
build-docker-image-no-compile:  ## Build the docker image with nginx, python api server and the compiled frontend in it. Skip compilation of the frontend (build outside of the devcontainer).
	docker build -t oneshot-web .

.PHONY: build-docker-image
build-docker-image: compile-frontend build-docker-image-no-compile  ## Build the docker image with nginx, the python api server and the compiled frontend in it.
	echo "Done."

.PHONY: start-docker-image-bash
start-docker-image-bash: build-docker-image-no-compile  ## Start the docker but run bash instead. Inside the container, run the api with `pipenv run python src/main.py`, nginx with `nginx -g 'daemon off;'` or both with `/usr/bin/supervisor`. Make sure that the frontend was compiled before.
	mkdir -p ./_local_volume/api
	docker run --rm -it --name os-web -e TZ="Europe/Berlin" -e DATABASE_HOST="os-web-db" -e POSTGRES_PASSWORD="password" -e HOST_URL="localhost:8080" -e STAGE="qa" --volume=./_local_volume/api/:/srv/oneshot -p 8080:80 --network=os-web-db oneshot-web /bin/bash

.PHONY: start-docker-image
start-docker-image: build-docker-image-no-compile  ## Start the docker image. Make sure that the frontend was compiled before.
	mkdir -p ./_local_volume/api
	docker run --rm --name os-web -e TZ="Europe/Berlin"  -e DATABASE_HOST="os-web-db" -e POSTGRES_PASSWORD="password" -e HOST_URL="localhost:8080" -e STAGE="qa" --volume=./_local_volume/api/:/srv/oneshot -p 8080:80 --network=os-web-db oneshot-web

.PHONY: container-attach-bash
container-attach-bash:  ## Attach a shell to the docker container.
	docker exec -it os-web /bin/bash


.PHONY: start-docker-postgres
start-docker-postgres:  ## Start the docker image from Docker Hub.
	mkdir -p ./_local_volume/db
	docker run --rm --name os-web-db -e POSTGRES_PASSWORD="password" --volume=./_local_volume/db/:/var/lib/postgresql/data/ --volume=./container-assets/init.sql:/docker-entrypoint-initdb.d/init.sql --network=os-web-db postgres:latest

.PHONY: ping-postgres
ping-postgres:  ## Ping the postgres-container from within the devcontainer.
	ping os-web-db


.PHONY: start-docker-compose-stack
start-docker-compose-stack: build-docker-image-no-compile  ## Start the docker image and database with docker compose. Make sure that the frontend was compiled before.
	mkdir -p ./_compose_volume
	docker compose up --remove-orphans --no-deps --build


.PHONY: pull-and-start-docker-image
pull-and-start-docker-image:  ## Start the docker image from Docker Hub.
	# mkdir -p ./_local_volume/api
	docker run --rm -e TZ="Europe/Berlin" -e HOST_URL="localhost:8080" -e STAGE="prod" -p 8080:80 ptrlx/oneshot-web # --volume=./_local_volume/api/:/srv/oneshot 


.PHONY: build-frontend-android
build-frontend-android:  ## Build the frontend for android 
	cd frontend && VITE_DEPLOYMENT_MODE=ANDROID_EMULATOR ionic capacitor build android --no-open

.PHONY: build-frontend-android-prod
build-frontend-android-prod:  ## Build the frontend for android for production
	cd frontend && VITE_DEPLOYMENT_MODE=ANDROID_PROD ionic capacitor build android --prod --no-open
