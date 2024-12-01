#!/usr/bin/env sh

alembic upgrade head

uvicorn api.main:app --host 0.0.0.0 -p 4001