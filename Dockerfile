FROM python:3.8-alpine
COPY requirements.txt requirements.txt
COPY Makefile Makefile
RUN apk add --no-cache make
RUN pip3 install -r requirements.txt
