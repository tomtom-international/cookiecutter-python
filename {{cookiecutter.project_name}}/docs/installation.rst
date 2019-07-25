.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `{{ cookiecutter.vs|title }} repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone ssh://git@{{ cookiecutter.vs_url }}{% if cookiecutter.vs|lower == "bitbucket" %}:7999{% endif %}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}.git

{% if cookiecutter.vs|lower == "github" -%}
Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/tarball/master

{% endif -%}

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


{% if cookiecutter.vs|lower == "github" -%}
.. _{{ cookiecutter.vs|title }} repo: https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}
.. _tarball: https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}/tarball/master
{% elif cookiecutter.vs|lower == "bitbucket" -%}
.. _{{ cookiecutter.vs|title }} repo: https://{{ cookiecutter.vs_url }}/projects/{{ cookiecutter.vs_account }}/repos/{{ cookiecutter.project_name }}
{% endif -%}
