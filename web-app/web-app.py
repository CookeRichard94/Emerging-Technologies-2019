# Richard Cooke
# G00331787

# Flask web app to that reads the data in the static html page and passes it to the model in the jupyter notebook

# Importing flask
import flask as fl

# Used to plot data
import numpy as np

import base64

from keras.models import load_model

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('web-app.html')

app.run()