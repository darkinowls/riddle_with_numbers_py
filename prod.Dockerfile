FROM python:3.11-alpine3.19

WORKDIR /program

COPY pyproject.toml .

RUN python -m venv .venv
RUN source .venv/bin/activate
ENV PATH="/program/.venv/bin:$PATH"

ENV pythonunbuffered 1



RUN pip install poetry
RUN poetry install


COPY app /program/app
#COPY tests /app/tests
#COPY migrations /app/migrations
COPY Makefile .
