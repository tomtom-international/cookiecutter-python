ARG PYTHON_BASE=python:3.6.7-alpine3.7

FROM tomtom-docker-registry.bintray.io/python/python3-pkg-builder:0.0.22 AS builder
COPY requirements_dev.txt /
RUN pip install -r /requirements_dev.txt


FROM $PYTHON_BASE AS deploy_builder
RUN pip install --upgrade virtualenv==16.4.3 && python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /code
WORKDIR /code
RUN python setup.py sdist \
  && pip install dist/*


FROM $PYTHON_BASE
COPY --from=deploy_builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT []
