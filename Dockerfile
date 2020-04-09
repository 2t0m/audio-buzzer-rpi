FROM arm32v7/python:3.6.4-slim-jessie

RUN apt-get update && apt-get install -y python-dev python3-dev build-essential pkg-config libfreetype6-dev libpng12-dev
RUN pip3 install RPi.GPIO time configparser

RUN mkdir app

WORKDIR /app
COPY gpio.py buzz.py
CMD ["python", "./buzz.py"]
