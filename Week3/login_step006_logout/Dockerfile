FROM python:3.9-alpine
COPY . /code
WORKDIR /code

RUN apk add build-base


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD flask run --host=0.0.0.0
