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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
