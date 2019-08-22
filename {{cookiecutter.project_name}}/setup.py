#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import {{ cookiecutter.project_slug }}


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as changelog_file:
    changelog = changelog_file.read()

requirements = []
extra_requirements = {}
# Ensure that linting and testing will be done with all depedencies installed
collected_extras = []
for req_set in extra_requirements.values():
    collected_extras += req_set

# pytest-runner is needed to be able to call `python setup.py test` and use pytest to
# execute the tests
setup_requirements = ["pytest-runner",] + collected_extras
test_requirements = ["pytest", "pytest-cov", "coverage",]


setup(
    name={{ cookiecutter.project_slug }}.__project__,

    # Versions should comply with PEP440.
    version={{ cookiecutter.project_slug }}.__version__,

    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    {% if cookiecutter.vs|lower == "github" -%}
    url="https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}",
    {% elif cookiecutter.vs|lower == "bitbucket" -%}
    url="https://{{ cookiecutter.vs_url }}/projects/{{ cookiecutter.vs_account }}/repos/{{ cookiecutter.project_name }}",
    {% endif -%}

     # Author details
    author={{ cookiecutter.project_slug }}.__author__,
    author_email={{ cookiecutter.project_slug }}.__email__,

    # Choose your license
    license="Apache Software License 2.0",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    # What does your project relate to?
    keywords="{{ cookiecutter.project_slug }}",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={},

    # If set to True, this tells setuptools to automatically include any data
    # files it finds inside your package directories that are specified by your MANIFEST.in file.
    # See as well https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files.
    include_package_data=True,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_name }}={{ cookiecutter.project_slug }}.cli:main",
        ],
    },

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # Please pin to specific versions.
    install_requires=requirements,

    # List of dependencies required before running the setup script.
    setup_requires=setup_requirements,

    # List of dependencies required during test execution.
    tests_require=test_requirements,

    # Name a package or module containing one or more tests
    test_suite="tests"
)
