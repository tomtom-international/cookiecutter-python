#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_dir(path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, path))

if __name__ == '__main__':

    if "{{ cookiecutter.vs }}".lower() == "bitbucket":
        remove_dir(".github")

    if "{{ cookiecutter.ci }}".lower() == "azure":
        remove_file("Jenkinsfile")

    if "{{ cookiecutter.ci }}".lower() == "jenkins":
        remove_file("azure-pipelines.yml")
