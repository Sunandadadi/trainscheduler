from flask import Flask, jsonify, request

from utils.helper import Helper
from configuration.default import Settings

app = Flask(__name__)

@app.route('/')
def index():
    return Settings.WELCOME_TEXT

@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.json
        Settings.logger.info(f"Path: {request.path} called with args: {data}")
        a = Helper(data)
        a.add_train_data()
        Settings.logger.info(f"Successfully Processed data: {data}")
        return jsonify(Settings.ADD_SUCCESS_TEXT), 200

    except Settings.DEFINED_EXCEPTIONS as e:
        Settings.logger.error(str(e))
        Settings.logger.error("Returned with status code 400")
        return jsonify(str(e)), 400

    except Exception as e:
        Settings.logger.error(str(e))
        Settings.logger.error("Returned with status code 500")
        return jsonify(str(e)), 500

@app.route('/fetch', methods=['GET'])
def fetch():
    try:
        data = request.args
        Settings.logger.info(f"Path: {request.path} called with args: {data}")
        a = Helper(data)
        result = a.fetch_simultaneous_trains()
        Settings.logger.info(f"Successfully Processed data: {data}, with return value: {result}")
        return jsonify(result), 200

    except Settings.DEFINED_EXCEPTIONS as e:
        Settings.logger.error(str(e))
        Settings.logger.error("Returned with status code 400")
        return jsonify(str(e)), 400

    except Exception as e:
        Settings.logger.error(str(e))
        Settings.logger.error("Returned with status code 500")
        return jsonify(str(e)), 500

@app.errorhandler(404)
def page_not_found(error):
    Settings.logger.error(f"Reached unknow path: {request.path}")
    Settings.logger.error("Returned with status code 404")
    return jsonify('Oops! Page not found'), 404

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
