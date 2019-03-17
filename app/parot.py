#!/usr/bin/env python3

import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def talk():
    version = os.getenv("VERSION")
    return "Knative says this is app " + str(version)
