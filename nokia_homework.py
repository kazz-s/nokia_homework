"""
Homework from Nokia
"""
from flask import (
    Flask,
    render_template,
    jsonify,
)
import requests

APP = Flask(__name__)


@APP.route('/')
def index():
    """
    Main view.

    :return: Response
    """
    json_response = requests.get('https://httpbin.org/get').json()

    return jsonify(json_response)


@APP.route('/fail')
def fail():
    """
    View for testing Exception handling

    :return: Response
    """
    raise Exception


@APP.errorhandler(404)
def error404(error):
    """
    View for 404 page

    :return: Response
    """
    msg = 'Page not found {}'.format(error)
    APP.logger.error(msg)
    return render_template('404.html'), 404


@APP.errorhandler(500)
def error500(error):
    """
    View for 500 page

    :return: Response
    """
    msg = 'Internal server error {}'.format(error)
    APP.logger.error(msg)
    return render_template('error.html', msg=msg), 500


@APP.errorhandler(requests.exceptions.ConnectionError)
def connection_error(error):
    """
    View for 500 page when Connection Error happens

    :return: Response
    """
    msg = 'There was a Connection Error: {}'.format(error.args)
    APP.logger.error(msg)
    return render_template('error.html', msg=msg), 500


@APP.errorhandler(Exception)
def ex(error):
    """
    View for 500 page with other Exceptions

    :return: Response
    """
    APP.logger.error("Exception happen")
    return render_template('error.html', msg=error.args), 500


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80)
