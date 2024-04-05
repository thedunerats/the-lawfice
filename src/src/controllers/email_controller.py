import smtplib
from email.mime.text import MIMEText
import logging

import werkzeug.exceptions
from flask_cors import cross_origin

# We also need to import the app (we called it flask_app in app.py) as we just want to reuse our existing
# instance of Flask
from src.app import *


# In order to access the request body and head, we will import "request" from flask

# from flask import request, make_response, jsonify
#
#
# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Headers", "*")
#     response.headers.add("Access-Control-Allow-Methods", "*")
#     return response
#
#
# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     return response

@flask_app.route("/controller", methods=['GET'])
def hit_controller():
    return 'Made it to new controller!'


# Let's create an endpoint which receives the form data on our home page and sends an email.
# @flask_app.route('/email', methods=['OPTIONS', 'POST'])
# def send_email():
# phone_number = request.form.get('your-phone')
# name = request.form.get('your-name')
# subject = request.form.get('your-case')
# email = request.form.get('your-email')
# body = request.form.get(
#     'your-message') + '\nMy name is ' + name + '. Call me at' + phone_number + '.' + 'or email me at ' + email
# s = smtplib.SMTP('smtp.uk.xensource.com')
# s.set_debuglevel(1)
# msg = MIMEText(body)
# sender = 'me@example.com'
# recipients = ['scott@bassinlaw.net', 'doug@bassinlaw.net', 'thedunerats@yahoo.com']
# msg['Subject'] = subject
# msg['From'] = sender
# msg['To'] = ", ".join(recipients)
# s.sendmail(sender, recipients, msg.as_string())
# return 'Email sent!'
# response = flask_app.jsonify({'some': 'data'})
# return response
# if request.method == "OPTIONS":  # CORS preflight
#     return _build_cors_preflight_response()
# elif request.method == "POST":  # The actual request following the preflight
#     return _corsify_actual_response(jsonify({'some': 'data'}))
# else:
#     raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

@flask_app.errorhandler(werkzeug.exceptions.NotFound)
def handle_404(error):
    return '404 Not Found: No such resource exists on this server!', 404
