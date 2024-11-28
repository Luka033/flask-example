from flask import Flask
import os

application = Flask(__name__)

@application.route('/')
def hello_world():
    stage = os.environ.get('STAGE')
    return f'Here is my test environment variable: {stage}'