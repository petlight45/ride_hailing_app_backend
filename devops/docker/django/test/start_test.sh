#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

coverage run --source='app' manage.py test app.tests
coverage report -m
