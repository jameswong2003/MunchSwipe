from flask import Flask, render_template, url_for, request
from yelp_api import Yelp
import config

API_KEY = config.api_key

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('intdex.html')

if __name__ == "__main__":
    app.run(debug=True)