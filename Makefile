.PHONY: help prepare-dev test lint run
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import webbrowser, sys

webbrowser.open(sys.argv[1])
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON_PATH=/usr/local/bin/python3.6
PYTHON=${VENV_NAME}/bin/python3.6

clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

install: ## Install dependencies.
	${VENV_ACTIVATE}
	pip install --upgrade pip
	pip install -r requirements.txt

lint: ## Lint project.
	${PYTHON} -m flake8
	${PYTHON} -m pylint run.py

mvenv: ## Create virtual environment.
	virtualenv -p ${PYTHON_PATH} venv

run: ## Run application.
	${PYTHON} run.py

test: ## Run tests.
	${PYTHON} -m pytest
