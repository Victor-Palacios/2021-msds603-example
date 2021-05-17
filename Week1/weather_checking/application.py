import datetime
from flask import Flask
from flask import render_template, render_template_string, redirect
import boto3
import time
import requests
import json
import os

from user_definition import *

application = Flask(__name__)

def read_s3_obj(bucket_name, output_file):
    """ Read from s3 bucket"""
    try:
        session = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )
        s3 = session.resource('s3')
        print("connected")
        obj = s3.Object(bucket_name, output_file)
        body = obj.get()['Body'].read().decode('utf-8')
        return body
    except:
        print("not")
        return ""



@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    """ index page -- shown on the beginning """
    body = read_s3_obj(bucket_name, output_file)

    #s3 = boto3.resource('s3')
    #obj = s3.Object(bucket_name, output_file)
    #body = obj.get()['Body'].read().decode('utf-8')

    return render_template('index.html', output=body)


@application.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """ Read Google Distance API """
    api_key = os.environ['API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&zip={zip},us&units=imperial"
    response = requests.get(url)
    x = response.json()
    print(url)
    print(x)
    main = x['weather'][0]['main']
    temp = x['main']['temp']

    if (main in ['Clear', 'Clouds'] and 60 < temp < 85):
        msg = "Go for a walk"
    else:
        msg ="Stay home"
    prev_reading = read_s3_obj(bucket_name, output_file)
    print(prev_reading)

    body = "{}\t{}\t{}\t{}\t{}\n".format(msg,
                                           datetime.datetime.now(),
                                           main,
                                           temp,
                                           prev_reading)


    #s3 = boto3.resource("s3").Object(bucket_name,output_file).put(Body=body)
    boto3.resource("s3").Bucket(bucket_name).put_object(Key=output_file, Body=body, ACL='public-read-write')

    time.sleep(5) # Added this for working on EB - Needs a delay to update the access after putting an obj

    return redirect("/index")

if __name__ == '__main__':
    application.jinja_env.auto_reload = True
    application.config['TEMPLATES_AUTO_RELOAD'] = True
    application.debug = True
    application.run(host ='0.0.0.0', port = 80, debug = True)