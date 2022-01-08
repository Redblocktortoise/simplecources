# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR /simpledjango
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
