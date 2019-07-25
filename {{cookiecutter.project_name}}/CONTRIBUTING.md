# Contributing

Contributions are welcome, and they are greatly appreciated. Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

{% if cookiecutter.vs|lower == "github" -%}
### Report Bugs

Report bugs at https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account}}/{{ cookiecutter.project_name }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and
"help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement
it.

{% endif -%}
### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation,
whether as part of the official {{ cookiecutter.project_name }} docs,
in docstrings, or even on the web in blog posts, articles, and such.

{% if cookiecutter.vs|lower == "github" -%}
### Submit Feedback

The best way to send feedback is to file an issue at
https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{cookiecutter.project_name }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

{% endif -%}
## Get Started

Ready to contribute? Here's how to set up **{{cookiecutter.project_name }}** for local development.

1. Fork the **{{ cookiecutter.project_name }}** repo on {{ cookiecutter.vs | title }}.

2. Clone your fork locally:

        $ git clone ssh://git@{{ cookiecutter.vs_url }}{% if cookiecutter.vs|lower == "bitbucket" %}:7999/~{% else %}/{% endif %}your_name_here/{{ cookiecutter.project_name }}.git

3. Install your local copy into a virtualenv. Assuming you have virtualenv installed,
   this is how you set up your fork for local development:

        $ cd {{ cookiecutter.project_name }}/
        $ virtualenv env
        $ source env/bin/activate
        $ python setup.py develop

4. Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

5. When you're done making changes, check that your changes pass pylint
   and the tests, including testing other Python versions with tox:

        $ tox

  To get tox, just pip install it into your virtualenv.

6. Commit your changes and push your branch to {{ cookiecutter.vs | title }}:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the {{ cookiecutter.vs | title }} website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in README.md.
3. The pull request should work for Python 3.5, 3.6 and 3.7, and for PyPi. Check {% if cookiecutter.ci|lower == "azure" -%}https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build{% elif cookiecutter.ci|lower == "jenkins" -%}{{ cookiecutter.ci_url }}/{% if cookiecutter.ci_org_name|length -%}job/{{ cookiecutter.ci_org_name }}/{% endif %}job/{{ cookiecutter.ci_project_name }}/job/{{ cookiecutter.project_name }}/view/change-requests/{% endif %} and make sure that the tests pass for all supported Python versions.



## Tips

To run a subset of tests:

    $ py.test tests/test_{{ cookiecutter.project_slug }}.py

## Deploying

Deployment can only be done by the project maintainers and is done on-demand via the {{ cookiecutter.ci | title }} CI.

{% if cookiecutter.ci|lower == "azure" -%}
Select the [{{ cookiecutter.project_name }} build pipeline](https://dev.azure.com/{{ cookiecutter.ci_org_name }}/{{ cookiecutter.ci_project_name }}/_build) and click
on the **Queue** button and run a build with the following settings:

* Branch: `master`
* Commit: leave it empty
* Variables:
  * `release: true`

{% elif cookiecutter.ci|lower == "jenkins" -%}
Go to the [{{ cookiecutter.project_name }} Jenkins job]({{ cookiecutter.ci_url }}/{% if cookiecutter.ci_org_name|length -%}job/{{ cookiecutter.ci_org_name }}/{% endif %}job/{{ cookiecutter.ci_project_name }}/job/{{ cookiecutter.project_name }}/job/master)
and click on **Build with parameters**, tick **doRelease** and click the **Build** button.
{% endif -%}
