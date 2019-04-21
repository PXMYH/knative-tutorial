#!/usr/bin/env python3

import os
from flask import Flask
app = Flask(__name__)


@app.route('/version')
def version():
    version = os.getenv("VERSION")
    return "Knative says this is app " + str(version)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
