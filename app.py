from flask import Flask, render_template, request, redirect
from yelp_api import Yelp

# Configuration for API Key
import config
API_KEY = config.api_key

app = Flask(__name__)

# Index Page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form['location'])
        # return redirect('/result')
    return render_template('index.html')

# Result Page for results
@app.route('/result')
def result():
    obj_dump = Yelp.search(API_KEY, term='', location='')
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)