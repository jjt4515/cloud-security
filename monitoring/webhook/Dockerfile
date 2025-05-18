FROM python:3.11-slim

WORKDIR /app

COPY webhook_handler.py .

RUN pip install flask

EXPOSE 5001

CMD ["python", "webhook_handler.py"]