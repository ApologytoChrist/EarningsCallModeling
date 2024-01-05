from flask import Flask, jsonify

import EarningsTracker
from EarningsTracker import *
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)


@app.route('/')
def hello_world():
    return "Good Morning"

@app.route('/api/data')
def get_data():  # put application's code here
    data = EarningsTracker.process()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=3000)
