@echo off
docker run --rm -v "%CD%:/app" -w /app python:3.11-slim python analyzer.py %*
