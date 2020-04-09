FROM python:3.8.0-slim

RUN apt-get update && apt-get install -y apt-utils python-dev python3-dev build-essential pkg-config
RUN pip3 install RPi.GPIO configparser

RUN mkdir app

WORKDIR /app
COPY gpio.py buzz.py
CMD ["python", "./buzz.py"]
