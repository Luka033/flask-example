from flask import Flask
import os

application = Flask(__name__)

@application.route('/')
def hello_world():
    mail_username = os.environ.get('MAIL_USERNAME')
    return f'Here is my test environment variable: {mail_username}'