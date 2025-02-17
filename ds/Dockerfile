FROM python:3.12

WORKDIR /ds

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config  virtualenvs.create false && \
    poetry install --no-root

COPY . .