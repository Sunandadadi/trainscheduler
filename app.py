from flask import Flask, jsonify, request
import logging

from utils.helper import Helper
from configuration.default import Settings

app = Flask(__name__)
logger = logging.getLogger(__name__)

# TODO: Fix logging. Add logs to file

@app.route('/')
def index():
    return Settings.WELCOME_TEXT

@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.json
        logging.info(f"{request.path} called with args: {data}")
        a = Helper(data)
        a.validate_add_request()
        a.add_train_data()
        return Settings.WELCOME_TEXT
    except Exception as e:
        logger.error(str(e))
        return jsonify(str(e)), 400

@app.errorhandler(404)
def page_not_found(error):
    return jsonify('Oops! Page not found'), 404

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
