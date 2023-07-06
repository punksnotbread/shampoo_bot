FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy as base

FROM base as builder

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_VERSION=1.5.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry check

COPY src/ ./src/
COPY README.md ./

RUN poetry install --without dev

FROM builder as runtime
WORKDIR /app

COPY .env ./

CMD ["poetry", "run", "python", "-m", "shampoo_scraper.main"]
