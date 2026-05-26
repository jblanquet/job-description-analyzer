docker run --rm `
    -v "${PWD}:/app" `
    -w /app `
    python:3.11-slim `
    python analyzer.py @args
