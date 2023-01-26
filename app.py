from flask import Flask, render_template, redirect, request, url_for
from yelp_api import Yelp
import json
import random

# Configuration for API Key
import config
API_KEY = config.api_key

database_path = 'database/data.json'
app = Flask(__name__)

# Index Page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        obj_dump = Yelp.search(api_key=API_KEY, term=request.form['term'], location=request.form['location'])
        # Dump data into a database
        with open(database_path, 'w') as outfile:
            json.dump(obj_dump, outfile, indent=4)
        return redirect('/result')
    
    return render_template('index.html')

# Result Page for results
@app.route('/result')
def result():
    # Choose random result from database
    with open(database_path, 'r') as f:
        data = json.load(f)
        result = random.choice(data['businesses'])
    return result

if __name__ == "__main__":
    app.run(debug=True)