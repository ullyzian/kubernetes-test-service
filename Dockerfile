FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y postgresql-client

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
