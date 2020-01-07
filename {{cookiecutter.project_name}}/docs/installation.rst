.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install{% if "artifactory" in cookiecutter.pypi_repo %} -i {{ cookiecutter.pypi_repo }}{% endif %} {{ cookiecutter.project_name }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

Checkout the `{{ cookiecutter.project_name }}`_ from {{ cookiecutter.vs|title }}.

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


{% if cookiecutter.vs|lower == "github" -%}
.. _{{ cookiecutter.project_name }}: https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}
.. _tarball: https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/tarball/master
{% elif cookiecutter.vs|lower == "bitbucket" -%}
.. _{{ cookiecutter.project_name }}: https://{{ cookiecutter.vs_url }}/projects/{{ cookiecutter.vs_account }}/repos/{{ cookiecutter.project_name }}
{% endif -%}
