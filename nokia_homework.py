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

    return jsonify(json_response)


@app.route('/fail')
def fail():
    raise Exception


@app.errorhandler(404)
def error404(e):
    msg = 'Page not found {}'.format(e)
    app.logger.error(msg)
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(e):
    msg = 'Internal server error {}'.format(e)
    app.logger.error(msg)
    return render_template('error.html', msg=msg), 500


@app.errorhandler(requests.exceptions.ConnectionError)
def connection_error(e):
    msg = 'There was a Connection Error'
    app.logger.error(msg)
    return render_template('error.html', msg=msg), 500


@app.errorhandler(Exception)
def ex(e):
    app.logger.error("Exception happen")
    return render_template('error.html', msg=e.args), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
