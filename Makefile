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
	cd backend/api && pipenv install

.PHONY: start-api
start-api:  ## Start the api
	cd backend/api && pipenv run python src/main.py

.PHONY: setup-frontend
setup-frontend:  ## Setup the frontend
	# todo npm install

.PHONY: start-frontend
start-frontend:  ## Start the frontend
	cd frontend && ionic serve
