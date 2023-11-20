# BASE
FROM python:3.11-slim as base

ENV APP_ROOT="/opt/webapp" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV PATH="$APP_ROOT/.venv/bin:$PATH"

# BUILDER 
FROM base as builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR ${APP_ROOT}

COPY pyproject.toml poetry.lock ${APP_ROOT}/
COPY app $APP_ROOT/app

RUN poetry install --without dev
RUN rm -rf $POETRY_CACHE_DIR

# DEVELOPMENT
FROM builder as dev

ENV SANIC_ENV=development

WORKDIR ${APP_ROOT}

EXPOSE 8000
