# Richard Cooke
# G00331787

#env FLASK_APP=web-app.py flask run

# Flask web app to that reads the data in the static html page and passes it to the model in the jupyter notebook

# Importing flask
import flask as fl

# Used to plot data
import numpy as np

import base64

from keras.models import load_model


model = load_model('../digit_reader.h5')

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('web-app.html')

@app.route('/predictedNumber', methods=['POST'])
def convertImage():
    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]

    # decode the dataURL
    # remove the added part of the url start from the 22 index of the image array
    decodedImage = base64.b64decode(encodedImage[22:])

    # save the image
    with open('image.png', 'wb') as f:
        f.write(decodedImage)
    
    return encodedImage

app.run()