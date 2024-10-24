FROM python:3.9.7-slim-buster

WORKDIR /usr/src/app/server
ENV FLASK_APP=main

COPY /app/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt