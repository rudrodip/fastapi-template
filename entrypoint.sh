#!/bin/sh
export PYTHONPATH=/app

prisma generate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4