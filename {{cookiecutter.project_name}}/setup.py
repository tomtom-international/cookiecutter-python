#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from __future__ import with_statement

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

setup_requirements = ["pytest-runner",]

test_requirements = ["pytest", "pytest-cov", "coverage",]

setup(
    author={{ cookiecutter.project_slug }}.__author__,
    author_email={{ cookiecutter.project_slug }}.__email__,
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
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_name }}={{ cookiecutter.project_slug }}.cli:main",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name={{ cookiecutter.project_slug }}.__project__,
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    {% if cookiecutter.vs|lower == "github" -%}
    url="https://{{ cookiecutter.vs_url }}/{{ cookiecutter.vs_account }}/{{ cookiecutter.project_name }}",
    {% elif cookiecutter.vs|lower == "bitbucket" -%}
    url="https://{{ cookiecutter.vs_url }}/projects/{{ cookiecutter.vs_account }}/repos/{{ cookiecutter.project_name }}",
    {% endif -%}
    version={{ cookiecutter.project_slug }}.__version__,
    zip_safe=False,
)
