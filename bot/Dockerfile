FROM python:3.10-slim-buster as builder

RUN apt-get update


RUN pip install poetry
COPY poetry.lock pyproject.toml /

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-dev\
    && rm -rf pyproject.toml poetry.lock

WORKDIR /bot
COPY . /bot

FROM builder as dev

CMD uvicorn api.main:app --host 0.0.0.0 --port 8000

FROM builder as test

RUN pip install pytest pytest-cov
RUN pytest --cov=app
RUN coverage report
RUN coverage xml