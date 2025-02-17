# ---------------------------------------------------------------------------------------------------------------------
# Build commands
# ---------------------------------------------------------------------------------------------------------------------

# Build docker image
build:
	docker-compose -f docker-compose.yaml build

build-test:
	ls && docker-compose -f devops/docker/docker-compose-test.yaml build

# Tear down the stack
down:
	docker-compose -f devops/docker/docker-compose.yaml down


# ---------------------------------------------------------------------------------------------------------------------
# Django execution commands
# ---------------------------------------------------------------------------------------------------------------------

# Run migrations
django-migrate:
	docker-compose -f devops/docker/docker-compose.yaml run --rm backend python manage.py migrate


# ---------------------------------------------------------------------------------------------------------------------
# Tests execution commands
# ---------------------------------------------------------------------------------------------------------------------

# Run tests locally
test-execute:
	docker-compose -f devops/docker/docker-compose-test.yaml run --rm backend coverage run --source='django.app' manage.py test app.tests && coverage report -m
