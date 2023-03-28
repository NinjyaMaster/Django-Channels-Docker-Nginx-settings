FROM python:3.9-alpine3.13
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN apk add --no-cache build-base linux-headers \
   && mkdir /code \
   && pip install --upgrade pip \
   && pip install wheel \
   && pip install uwsgi \
   && apk del build-base linux-headers
RUN pip install daphne
# RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python manage.py migrate