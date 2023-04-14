FROM python:3.10-slim-buster

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get clean

RUN pip install --upgrade pip
RUN pip install -U setuptools

COPY . .
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 main:app -k uvicorn.workers.UvicornWorker