.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

# Mandatory tools
PIP := $(shell command -v pip3 2> /dev/null)
PYTHON := $(shell command -v python3 2> /dev/null)

# Virtualenv config and wrappers
PYTHONVERSION := python3
PYTHONENV := env
ENVPYTHON := $(PYTHONENV)/bin/python
ENVPIP := $(PYTHONENV)/bin/pip

BROWSER := $(ENVPYTHON) -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup-checks:
ifndef PIP
$(error Missing pip. Installation guide can be found here https://pip.pypa.io/en/stable/installing/)
endif
ifndef PYTHON
$(error Missing python. Installation guide can be found here https://www.python.org/downloads/)
endif

setup: setup-checks ## install dev requirements
	$(PIP) install virtualenv
	virtualenv --python=$(PYTHONVERSION) $(PYTHONENV)
	$(ENVPIP) install -r requirements_dev.txt

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr env/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
{%- if cookiecutter.use_tox|lower == "y" -%}
	rm -fr .tox/
{%- endif %}
	rm -fr .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	$(ENVPYTHON) setup.py lint

test: ## run tests quickly with the default Python
	$(ENVPYTHON) setup.py test

{% if cookiecutter.use_tox|lower == "y" -%}
test-all: ## run tests on every Python version with tox
	tox
{% endif -%}

coverage: ## check code coverage quickly with the default Python
	$(ENVPYTHON) setup.py test
	coverage html --directory build/htmlcov
	$(BROWSER) build/htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	$(ENVPYTHON) setup.py sdist
	$(ENVPYTHON) setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	$(ENVPYTHON) setup.py install
