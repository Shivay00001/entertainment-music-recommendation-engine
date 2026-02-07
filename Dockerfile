FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir scikit-learn pandas

COPY . .

ENTRYPOINT ["python", "src/main.py"]
