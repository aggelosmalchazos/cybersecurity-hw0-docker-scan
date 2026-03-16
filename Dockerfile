FROM python:3.6-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]