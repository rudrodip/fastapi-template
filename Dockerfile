FROM python:3.10-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY prisma/ prisma/
RUN poetry run prisma generate

COPY . .

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]