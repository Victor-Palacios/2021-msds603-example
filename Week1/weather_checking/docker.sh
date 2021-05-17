#!/bin/bash
docker build -t weather-app .
docker tag weather-app dwoodbridge/weather-app
docker push dwoodbridge/weather-app
#docker run -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  -e API_KEY=$API_KEY -d -p 80:80 --name weather-app weather-app