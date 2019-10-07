{% set title = cookiecutter.project_name ~ ' documentation' -%}
{{ title }}
{% for _ in title %}={% endfor %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Readme <readme>
   installation
   usage
   Modules <modules>
   contributing
   history
{% if cookiecutter.open_source_project|lower == "y" -%}
   authors
{%- endif %}

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
