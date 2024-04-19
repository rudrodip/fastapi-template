FROM python:3.10-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copy only the poetry.lock and pyproject.toml files
COPY poetry.lock pyproject.toml ./
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install dependencies and cache the installed packages
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application code
COPY . .

# Expose the port
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]