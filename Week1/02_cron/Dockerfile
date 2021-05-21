FROM python:3.7-alpine

RUN apk --no-cache add curl
RUN apk add git

#RUN git clone https://github.com/dianewoodbridge/2021-msds603-example /2021-msds603-example
COPY . /2021-msds603-example/Week1/02_cron
WORKDIR /2021-msds603-example/Week1/02_cron

ADD cronjobs /cronjobs
COPY cron.sh /cron.sh
RUN chmod 755 /cron.sh /cronjobs
RUN crontab /cronjobs

CMD ["/cron.sh"]
