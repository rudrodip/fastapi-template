#!/bin/sh

# Check if the RELOAD environment variable is set
if [ "$RELOAD" = "True" ]; then
    # Development mode
    echo "Running in development mode with hot reloading..."
    export PYTHONPATH=/app
    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
    # Production mode
    echo "Running in production mode..."
    export PYTHONPATH=/app
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
fi