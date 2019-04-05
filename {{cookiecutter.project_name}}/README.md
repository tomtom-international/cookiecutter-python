# {{ cookiecutter.project_name }}

{% if cookiecutter.ci|lower == "azure" -%}
[![Azure DevOps builds](https://img.shields.io/azure-devops/build/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/{{cookiecutter.azure_build_definition_id }}.svg)](https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build/latest?definitionId={{cookiecutter.azure_build_definition_id }}&branchName=master)
[![Azure DevOps tests](https://img.shields.io/azure-devops/tests/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/{{cookiecutter.azure_build_definition_id }}.svg)](https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build/latest?definitionId={{cookiecutter.azure_build_definition_id }}&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/{{cookiecutter.azure_build_definition_id }}.svg)](https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build/latest?definitionId={{cookiecutter.azure_build_definition_id }}&branchName=master)
{% endif %}
{% if cookiecutter.vs|lower == "github" -%}
[![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Format](https://img.shields.io/pypi/format/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Status](https://img.shields.io/pypi/status/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyUp - Updates](https://pyup.io/repos/github/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/)
{% endif -%}
{% if cookiecutter.vs|lower == "bitbucket" -%}
[Bitbucket Pages](https://{{ cookiecutter.vs_url }}/pages/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/docs/browse/docs/index.html)
{% endif -%}

{{ cookiecutter.project_short_description }}

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [tomtom-international/cookiecutter-python](https://github.com/tomtom-international/cookiecutter-python) project template.
