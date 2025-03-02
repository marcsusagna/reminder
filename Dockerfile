FROM python:3.11-slim

ENV POETRY_VERSION=2.1.1

WORKDIR /reminder_app

COPY . .

RUN python3 -m pip install "poetry==$POETRY_VERSION"
RUN poetry install