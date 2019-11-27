# Richard Cooke
# G00331787

#env FLASK_APP=web-app.py flask run

# Flask web app to that reads the data in the static html page and passes it to the model in the jupyter notebook and returns a 
# prediction which should match the data passed from the html file

# Importing flask
import flask as fl


# Used to plot data
import numpy as np

# Used for encoding and decoding data
import base64

# Library of python bindings for visual problems
import cv2

# Imports from Python Image Library
from PIL import Image, ImageOps

#Used to import model in notebook
from keras.models import load_model

# Using load model import to bring in model created in notebook
model = load_model('../digit_reader.h5')

app = fl.Flask(__name__)

# Variables for resizing image to fit the mnist dataset
height = 28
width = 28
size = height, width

# Routing
# Route for home page
@app.route('/')
def home():
    # returns the static html file
    return fl.render_template('web-app.html')


@app.route('/predict', methods=['POST'])
def convertImage():
    # get the image from the request
    encoded = fl.request.values[('imgBase64')]

    # decode the dataURL
    # remove the added part of the url start from the 22 index of the image array
    decoded = base64.b64decode(encoded[22:])

    # save the image
    with open('image.png', 'wb') as f:
        f.write(decoded)
    
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
    grayScaleImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)
    grayScaleArray = np.array(grayScaleImage).reshape(1, 784)

    # setter and getter to return the predicition from the model
    setPrediction = model.predict(grayScaleArray)
    getPrediction = np.array(setPrediction[0])

    # np.argmax returns the highest value ie what should be the same as the digit passed
    predictedNumber = str(np.argmax(getPrediction))
    print(predictedNumber)

    # May attempt to return whole array with outputs like in model to determine what the model is predicting
    #predictedNumber = str((getPrediction))
    #print(predictedNumber)
    # This returns a one hot vector, with binary results, was hoping for an array of normalized percentages 

    # returns the predicted number to be passed to the .js file
    return predictedNumber
app.run()

# References
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python