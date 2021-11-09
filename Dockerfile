FROM python:3.7-slim

ENV APP_HOME /app

COPY ./backend /app
COPY ./requirements.txt /app

WORKDIR /app
ENV PORT 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
