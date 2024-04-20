# Build stage
FROM python:3.10-slim AS builder

RUN pip install --no-cache-dir poetry
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY prisma/ prisma/

RUN prisma generate

COPY . .

# Final stage
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]