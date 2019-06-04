ARG PYTHON_BASE=python:3.6.7-alpine3.7

# The *builder* image is used mainly by the [Jenkins Python pipeline](https://github.com/tomtom-international/jsl/blob/master/vars/pythonSetupPyPipeline.groovy)
# during the build & validation stages only. Removing it will result in a failure in Jenkins.
# This image can as well be used for local testing.
FROM tomtom-docker-registry.bintray.io/python/python3-pkg-builder:0.0.22 AS builder
COPY requirements_dev.txt /
RUN pip install -r /requirements_dev.txt

# The following two images are used to create the image that gets deployed to the Docker registry.
# The *deploy_builder* image installs the created source distribution package into an virtual
# environment so that it becomes easier to copy the modules and its dependencies to the image that
# gets deployed to the registry.
FROM $PYTHON_BASE AS deploy_builder
RUN pip install --upgrade virtualenv==16.6.0 && python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /code
WORKDIR /code
RUN python setup.py sdist \
  && pip install dist/*


FROM $PYTHON_BASE
COPY --from=deploy_builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT [""]
