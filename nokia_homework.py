from flask import (
    Flask,
    render_template,
    jsonify,
)
import requests

app = Flask(__name__)


@app.route('/')
def index():
    json_response = requests.get('https://httpbin.org/get').json()

    # return render_template('onewebpage.html', data=json_response)
    return jsonify(json_response)


@app.errorhandler(500)
def error500(e):
    msg = f'Internal server error {e}'
    app.logger.error(msg)
    return msg


@app.errorhandler(404)
def error500(e):
    msg = f'Page not found {e}'
    app.logger.error(msg)
    return msg


@app.errorhandler(Exception)
def ex(e):
    msg = f'Python exception {e}'
    app.logger.error(msg)
    return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
