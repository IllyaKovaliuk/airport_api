FROM python:3.9
LABEL maintainer="kovalukilla271@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR /airport_project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .