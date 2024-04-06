import smtplib
from email.mime.text import MIMEText

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from src.src.services.email_service import send_email, is_valid_email
from src.src.services.blog_service import create_blog_post
from src.src.services.phone_service import is_phone_number
from src.src.util.json_util import validate_email_request_json

# This is general Flask configuration. Note that you do not typically create several instances of
# the imported Flask class and that we are only doing it for today's demo.

# __name__ is a built-in variable which evaluates to the name of the current module. It is often used
# to determine whether the current script is being run on its own or being imported somewhere else. If
# a module is being directly run, __name__ evaluates to __main__.

# Setting the static_url_path like so will remove the "static" from your URL paths for static resources.
# We need to define a cross-origin header in order to receive POST and PUT requests.
flask_app = Flask(__name__, static_url_path='')
CORS(flask_app)


# Let's create a hello world "endpoint". An endpoint simply exposes a resource to a client under a specific,
# unique identifier.

# This function declaration and the accompanying "decorator" allow us to define a resource that this server
# exposes to the client. A decorator takes in a function, adds some additional functionality, and returns
# said function.

# We have defined this resource as a "welcome" resource at the root of our application. If we simply navigate
# to http://localhost:5000/ this resource is returned to the client.

# Please note that the return value for a route must be formatted as either a: string, dictionary, tuple,
# Response instance.


@flask_app.route('/')
def hello_world():
    # Writing to the response body
    return 'Made it!'


@flask_app.route('/test', methods=['GET'])
def test_endpoint():
    return 'Made it!'


@flask_app.route('/blogpost', methods=['POST'])
def post_to_blog():
    json = request.json
    create_blog_post(json['text'])


@flask_app.route('/email', methods=['POST'])
def format_and_send_email():
    json = request.json
    valid_request, failure_reason = validate_email_request_json(json)
    if not valid_request:
        return make_response(jsonify(failure_reason=failure_reason, status=400), 400)
    phone_number = json['your-phone']
    name = json['your-name']
    subject = json['your-case']
    email = json['your-email'] if is_valid_email(json['your-email']) else "No email provided"
    body = json['your-message'] + '\nMy name is ' + name + '. Call me at ' + phone_number + \
           ' or email me at ' + email
    recipients = ['scott@bassinlaw.net', 'doug@bassinlaw.net']
    # if not is_valid_email(email):
    #     return make_response(jsonify(failure_reason='INVALID EMAIL ADDRESS', status=406), 406)
    if not is_phone_number(phone_number):
        return make_response(jsonify(failure_reason='INVALID PHONE NUMBER', status=406), 406)
    response = send_email('doug@bassinlaw.net', recipients, subject, body)
    return make_response(jsonify(confirmation='Email sent!\nStatus code returned: ' + str(response.status_code),
                                 status=200), 200)
