from flask import Blueprint, render_template, request, jsonify, session
from datetime import datetime
import time
import bleach
import os
import uuid

from .ai_module import process_user_input

RATE_LIMIT_PER_HOUR = 60
RATE_LIMIT_WINDOW = 1800

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-east-1') 


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        message = request.form['text']
    return render_template('index.html', message=message)


@main.route('/ask', methods=['POST'])
def ask():
    # Rate limiting logic
    rate_limit = request.cookies.get('rate_limit', 0)
    last_request_time = request.cookies.get('last_request_time', 0)
    current_time = time.time()

    try:
        rate_limit = int(rate_limit)
        last_request_time = float(last_request_time)
    except ValueError:
        rate_limit = 0
        last_request_time = 0

    if rate_limit >= RATE_LIMIT_PER_HOUR and current_time - last_request_time < RATE_LIMIT_WINDOW:
        # If rate limit is exceeded, return an error message
        return jsonify({'error': 'Hourly rate limit exceeded. Please try again later.'}), 429
    elif current_time - last_request_time >= RATE_LIMIT_WINDOW:
        rate_limit = 0  # Reset the counter after an hour

    # Processing the user input
    user_input = request.json.get('input')
    sanitized_input = bleach.clean(user_input)
    
    # Assuming process_user_input() handles the main logic and returns the response
    response_messages = process_user_input(sanitized_input)

    # Create a response object to add cookies
    response = jsonify(response_messages)
    response.set_cookie('rate_limit', str(rate_limit + 1), max_age=RATE_LIMIT_WINDOW)
    response.set_cookie('last_request_time', str(current_time), max_age=RATE_LIMIT_WINDOW)

    return response