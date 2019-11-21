# Richard Cooke
# G00331787

#env FLASK_APP=web-app.py flask run

# Flask web app to that reads the data in the static html page and passes it to the model in the jupyter notebook

# Importing flask
import flask as fl

# Used to plot data
import numpy as np

import base64
import cv2

# Imports from Python Image Library
from PIL import Image, ImageOps

#Used to import model in notebook
from keras.models import load_model

# Using load model import to bring in model created in notebook
model = load_model('../digit_reader.h5')

app = fl.Flask(__name__)

height = 28
width = 28

size = height, width

# Routing
# Route for home page
@app.route('/')
def home():
    # returns the static html file
    return app.send_static_file('web-app.html')


@app.route('/predict', methods=['POST'])
def convertImage():
    # get the image from the request
    encodedImage = fl.request.values[('imgBase64')]

    # decode the dataURL
    # remove the added part of the url start from the 22 index of the image array
    decodedImage = base64.b64decode(encodedImage[22:])

    # save the image
    with open('image.png', 'wb') as f:
        f.write(decodedImage)
    
    # Open the recently created image
    userImage = Image.open("image.png")

    # Resize the image to fit the mnist dataset using imageOps import from PIL
    newImage = ImageOps.fit(userImage, size, Image.ANTIALIAS)

    # Other attempt for resizing image
    # newImage = userImage.thumbnail(size, Image.ANTIALIAS)

    # save the newly resized image
    newImage.save("imageResized.png")

    # cv2 loads the new images
    cv2Image = cv2.imread("imageResized.png")

    # Converting the new image to grayscale, reshaping and adding to nparray
    grayImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)
    grayArray = np.array(grayImage).reshape(1, 784)

    #
    setPrediction = model.predict(grayArray)
    getPrediction = np.array(setPrediction[0])

    #
    predictedNumber = str(np.argmax(getPrediction))
    print(predictedNumber)

    return predictedNumber
app.run()