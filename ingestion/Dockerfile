FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir pandas pyarrow sqlalchemy psycopg2-binary
COPY load_taxi.py .