# {{ cookiecutter.project_name }}

{% if cookiecutter.ci|lower == "azure" -%}
[![Build Status](https://dev.azure.com/tomtomweb/{{ cookiecutter.ci_org_name }}/_apis/build/status/{{ cookiecutter.ci_project_name }}/?branchName=master)](https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build/latest?definitionId={{cookiecutter.azure_build_definition_id }}&branchName=master)
{% endif %}
{% if cookiecutter.vs|lower == "github" -%}
[![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Format](https://img.shields.io/pypi/format/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Status](https://img.shields.io/pypi/status/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyUp - Updates](https://pyup.io/repos/github/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/)
{% endif -%}

{{ cookiecutter.project_short_description }}

## Features

* TODO

## Requirements

* [python3](https://www.python.org/downloads)
* [pip3](https://pip.pypa.io/en/stable/installing)
* [virtualenv >= 16.6.0](https://virtualenv.pypa.io/en/latest/installation/)

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [tomtom-international/cookiecutter-python](https://github.com/tomtom-international/cookiecutter-python) project template.
