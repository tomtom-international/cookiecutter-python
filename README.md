# Cookiecutter Python

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for Python packages.

* GitHub repo: https://github.com/tomtom-international/cookiecutter-python/
* Free software: Apache Software License 2.0

## Features

* Supports projects hosted in GitHub and BitBucket Server.
* Ready for [Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/) for GitHub projects and [Jenkins Declarative Pipelines](https://jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline) for internally hosted projects in BitBucket Server.
* Validation of your code
  * Testing based on `py.test`
  * Linting based on `pylint`
  * Formatting based on `black` (optional)
  * Spellchecking based on `pyenchant` (optional)
* Bumpversion: Pre-configured version bumping with a single command
* Auto-release to PyPI when PR gets merged into master via Azure Pipelines or Jenkins Pipelines
* Dependabot integration for Github based projects

### Experimental Features

* Tox: Setup to easily test for different Python version (currently only for 3.6)
* Makefile support for building, testing, releasing, etc.

### TODO

* Sphinx docs: Documentation ready for generation with, for example, ReadTheDocs

## Getting Started

### Prerequisites

Install the following minimum requirements

* [python3](https://www.python.org/downloads)
* [pip3](https://pip.pypa.io/en/stable/installing)
* [virtualenv >= 16.6.0](https://virtualenv.pypa.io/en/latest/installation/)

### Installing

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```bash
pip install cookiecutter
```

Generate the Python package project:

```bash
cookiecutter gh:tomtom-international/cookiecutter-python
```

Then:

* Create a repo and push the generated project to master.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``) and start coding.

#### Variables explained

Cookiecutter will prompt you for various settings which we are explained here:

* `full_name` -  The authors name (default: John Doe)
* `email` - The authors email (default: john.doe@example.com)
* `vs` - Select between github (1) or bitbucket (2) (default: 1)
* `vs_url` - Provide the domain name of the versioning system without `http(s)://` (default: github.com)
* `vs_account` - Account/organization on Github or project name on BitBucket Server (default: tomtom-international)
* `open_source_project` - Generate additional files for OSS project (AUTHORS.md, LICENSE, etc) (default: y for github, n for bitbucket)
* `project_name` - The name of your Python project. This is also the name of the repository in Github/BitBucket (default: python-skeleton)
* `project_slug` -  Python friendly module name. By default this is the normalized version of `project_name` (default: python_skeleton)
* `project_short_description` -  A short description of your Python package. This will end up in the README.md of your project
* `version` - The current in-development version. The project makes use of [SemVer](https://semver.org) (default: 0.0.1-dev)
* `use_black_formatter` - Use [black](https://github.com/psf/black) for formatting your code (default: n)
* `use_spellcheck` - Use [spellchecking](https://github.com/rfk/pyenchant) and user configurable dictionary in `.pylintrc` (default: n)
* `use_tox` - EXPERIMENTAL: Adds support for tox (default: n)
* `use_makefile` - EXPERIMENTAL: Adds support for Makefiles (default: n)
* `ci` - Select the CI system you want to use. By default the CI system is chosen based on the selected versioning system (`vs`). If you chose Github as VS the default CI system will be Azure Pipelines.  In case of Bitbucket you will get Jenkins.
* `ci_url` - URL to your CI system (eg. https://dev.azure.com, https://jenkins.acme.org)
* `ci_org_name` - For Azure Pipelines this is the organization name. In case of Jenkins you can leave this either empty or in case you have defined your Jenkins projects under a folder use the folder name.
* `ci_project_name` - For Azure Pipelines this is the name of your project. In case of Jenkins this is by default `vs_account` which usually is a `BitBucket Team Project`
* `pypi_repo` - PyPI repository the package should be deployed to. In case you select Github for `vs` the default value is the official PyPI index whereas in case of BitBucket you get a hint to provide a URL to an Artifactory PyPI repository.
* `pypi_credentials_id` - For Azure Pipelines this is the [service connection](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml) that allows you to push Python packages to the official PyPI index. For Jenkins this is the credentials ID used for authentication with an Artifactory PyPI repository.
* `docker_registry_credentials_id` - For Azure Pipelines this is the service connection that allows you to push Docker images to a public Docker registry. For Jenkins this is the credentials ID used for authentication with for example an Artifactory Docker repository.
* `jenkins_scm_credentials_id` -  Skip this for Azure Pipelines. For Jenkins this is the credentials ID for a user that has write access to a git repository. This is required to allow git commits/pushes during the versioning process.
* `azure_build_definition_id` - Skip this for Jenkins. For Azure Pipelines this is the ID identifiying the pipeline (eg. https://dev.azure.com/tomtomweb/GitHub-TomTom-International/_build?definitionId=26)

## Tips

### Azure

In order to use Azure DevOps/Pipelines, first create an [Azure DevOps account](https://azure.microsoft.com/en-us/services/devops), create an organization and project.

For detailed instructions please read the [Azure DevOps documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/overview?view=azure-devops).

#### Creating Azure Pipelines

A detailed description on how to create Azure Pipelines can be found as well [here](https://github.com/tomtom-international/azure-pipeline-templates/blob/master/README.md#creating-azure-pipelines).

**Remark**:
> In case you want to host a project in the `tomtom-international` organization and you chose Azure for the CI contact the @nav-pipeline team to request a build pipeline in the [TomTom Azure DevOps account](https://dev.azure.com/tomtomweb/GitHub-TomTom-International/_build).

### Jenkins

In case of hosting on Jenkins/Bitbucket Server we recommend using the *BitBucket Branch Source Plugin* that allows you to configure a folder in Jenkins that will scan the whole BitBucket project for repositories with a `Jenkinsfile`.

The following Jenkins plugins are required by the [`pythonSetupPyPipeline`](https://github.com/tomtom-international/jsl) used in the `Jenkinsfile`:

* `Warnings Next Generation Plugin >=4.0.0`
* `Cobertura Plugin >=1.13`
* `Pipeline: GitHub Groovy Libraries >=1.0`

## Credits

This package is inspired by [Cookiecutter PyPackage](https://github.com/audreyr/cookiecutter-pypackage/) project template.
