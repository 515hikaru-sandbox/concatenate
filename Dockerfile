FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV CONCATENATE_VERSION 0.9.2

RUN mkdir -p /app
WORKDIR /app
COPY concatenate.py /app/concatenate.py
COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "concatenate.py", "--help"]
