# Ride Hailing App

This project is a Django HTTP API server that exposes an endpoint which allows you to calculate a ride price
dynamically based on real-time factors such as demand, distance, and traffic conditions.


## Features

- **Unit Tests & Integration Tests**: Written with Django built-in testing framework unittests.
- **CI Pipeline**: Implemented with Github Actions.
- **Pre-Commit Hooks**: For Linting

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Server](#running-the-server)
- [Executing Tests](#executing-tests)
- [Test Coverage Reports](#test-coverage-reports)

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

```
git clone https://github.com/petlight45/ride_hailing_app_backend.git
```

2. **Change directory**

```
cd ride_hailing_app_backend
```

## Configuration

1. **Set up environmental variables**

For linux, Mac run

    ```
    cp ./envs/.env.example ./envs/.env
    ```

For Windows(cmd)

      ```
      copy envs\.env.example envs\.env
        ```

For Windows(PowerShell)

      ```
      Copy-Item -Path ./envs/.env.example -Destination ./envs/.env
        ```


Update the .env file with your local configuration values.

    DJANGO_SECRET_KEY = The secret key used for cryptographic signing in this Django app


    DJANGO_DEBUG = Whether the Django app runs in debug mode (True for development)


    DJANGO_ALLOWED_HOSTS = The list of allowed hostnames for this Django app


    DJANGO_CSRF_TRUSTED_ORIGINS = The trusted origins for CSRF protection


    DJANGO_SETTINGS_MODULE = The settings module to be used for this Django app


    DJANGO_USE_MEMORY_DATABASE = Whether to use an in-memory database for testing


    DJANGO_CORS_ALLOWED_ORIGINS = The allowed origins for Cross-Origin Resource Sharing (CORS)


    DJANGO_EXECUTION_ENVIRONMENT = The execution environment in which this Django app is running


    DJANGO_GUEST_ENDPOINT_API_KEY = The API key used to authenticate guest endpoint requests

## Running the Server

To run the server:
Without Docker;

After setting up virtual environments, run
```
    pip install -r requirements/local.txt

    python manage.py runserver
```


With Docker;
Install docker and docker compose on your operating environment

For linux, Windows or Mac run

    ```
    docker-compose up --build
    ```

Or(if the above failed)

      ```
      docker compose up --build
    ```


## Executing Tests

To execute the tests:
Without Docker;

After setting up virtual environments, run
```
    coverage run --source='app' manage.py test app.tests

    coverage report -m
```


With Docker;
Install docker and docker compose on your operating environment

For linux, Windows or Mac run

    ```
    docker compose -f ./devops/docker/docker-compose-test.yaml build

    docker compose -f devops/docker/docker-compose-test.yaml run --rm backend  "./start_test.sh"
    ```

Or(if the above failed)

      ```
       docker-compose run --rm backend  "./start_test.sh"
    ```

## Test Coverage Reports

To view coverage report as html

Open the file;
```
    htmlcov/index.html
```
