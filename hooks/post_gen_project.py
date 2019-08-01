#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def template_file(filename):
    return os.path.join(PROJECT_DIRECTORY, filename)


def file_size(filename):
    return os.stat(template_file(filename)).st_size


def remove_file(filepath):
    os.remove(template_file(filepath))


def remove_dir(path):
    shutil.rmtree(template_file(path))


if __name__ == "__main__":

    if "{{ cookiecutter.vs }}".lower() == "bitbucket":
        remove_dir(".github")

    if "{{ cookiecutter.ci }}".lower() == "azure":
        remove_file("Jenkinsfile")

    if "{{ cookiecutter.ci }}".lower() == "jenkins":
        remove_file("azure-pipelines.yml")

    if file_size("pyproject.toml") == 0:
        remove_file("pyproject.toml")
