# Digit Reader
## 1. Intro
This project was developed as part of the Emerging Technologies module at GMIT, in the Computing in Software Development course, year 4, it involves using the MNIST dataset to train a neural network to recognise hand-written digits sent to the network via a web app that allows the user to draw the digits. The neural network or model, will be created in python using the Keras library in Jupyter Notebook. The web app has been created using a  standard HTML, Javascript and CSS configuration. The model and the web app are connected via a python Flask server file which will connect the two by sending data from the web app to the neural network in the notebook.

## 2. Environment Set-up
For this application a number of necessary installs need to be made:

* Anaconda: Installed from [here](https://www.anaconda.com/distribution/) (Recommended that you install version 3.7 or newer)
  * Alternatively if you have already installed an older version of python, then enter the command line and enter the command ```conda update --all ```
* Keras/ Tensorflow: To install the necessary Keras/Tensorflow packages then follow the instructions in [this](https://web.microsoftstream.com/video/f6bd0f1c-802c-4c0a-bc54-211bc9d85ba5) or enter the following command into the command line ``` conda install -c conda-forge keras tensorflow ```
* OpenCV: To install OpenCV enter the command line and enter the command ```pip install opencv-python ```
* A comprehensive list of all necessary packages and versions of said packages is also provided within the ```requirements.txt``` file of this repository.

## 3. Research
### 3.1 Jupyter Notebook/Lab
Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. 
### 3.2 Keras
Keras is an open-source neural network library/API written in Python that runs on top of Tensorflow and PlaidML among others. It was created to be user friendly, easy to expand and for quick experimentation on neural networks. Keras is backed by many large companies such as Google, Microsoft and Amazon. Keras relies on back-end engines for lower level operations, in the case of this project we will be running Keras on Tensorflow 2.0.0
### 3.3 Tensorflow
Tensorflow is an open-source, python friendly, library that is used for numerical computation to make machine learning easier and faster. Tensorflow was created by the Google Brains team in 2015, it is designed to mix together machine learning and neural netwroking models together and making use of what they share in common. Tensorflows biggest benifit is that it uses abstraction to allow for increased re-usability. In the case of this project we will be using tensorflow for aiding in predicition of hand-written items.
### 3.4 MNIST
The MNIST dataset is a database of handwritten digits ranging from 0-9, priarily used for testing purposes. The dataset contains 60,000 training images and 10,000 testing images for a total of 70,000 images. Each image in the dataset has been normalized to fit into 28x28 pixel image. In the case of this project the MNIST dataset will be used as the base comparison for the sumbitted hand-written image, so the model created using keras and tensorflow can make a prediction on the entered digit.
### 3.5 OpenCV
OpenCV is an open-source computer vision and machine learning software library. OpenCV can be used for many things including recognizing and detecting human faces or counting the edges in an image. OpenCV is used by many large companies such as Google, Microsoft and Sony. In the case of this project OpenCV is used to convert the passed image to grayscale to allow the created model to more easily recognize the passed digit.
### 3.6 PIL
PIL is the Python Image Library. PIL is a core library for image manipulation in python. It is percieved as a less advanced image manipulation software than OpenCV. In the case of this project two of it's methods are used. The firs the Image function is used to open the image up for manipulation. The second ImageOps is used to reshape the passed image to 28x28 pixels so as to more closesly resemble the images that are found in the MNIST dataset.
### 3.7 Other
One-Hot vectors are arrays made of 0's and a single 1. The 1 in the index is used as the identifier to what is being pointed to. One-hot vectors are mainly used as they are easier for computers to read.    
Float32 is a 32 bit single-precision floating point. In the case of this project float32 is used to allow for more accurate division.   
Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format. In the case of this project Base64 is used to both encode and decode the image created by the web-app.
## 4. How to Run

* Download the repository by entering the command line and entering the command ```Git Clone https://github.com/CookeRichard94/Emerging-Technologies-2019 ```
* Using the command line enter the project folder by entering the command ``` cd Emerging-Technologies-2019 ```
* Change directory to the web-app folder by enter the command ``` cd web-app ```
* Run the web application by entering the command ``` python web-app.py ```
* The server application will be listening on ```http://127.0.0.1:5000/```, after the application has been run copy and paste this address to a browser and the application should run.
* Use the mouse to draw a digit from from the MNIST dataset (0-9), on the canvas provided, and then select the "Predict" button highlighted in green. The server should then make a prediction on which digit you have submitted.
* To make another prediction press the "Restart" button highlighted in yellow. This will clear the canvas and predicted number and allow for a new prediction to be made.

## 5. References
 * https://keras.io/
 * https://www.infoworld.com/article/3336192/what-is-keras-the-deep-neural-network-api-explained.html
 * https://www.infoworld.com/article/3278008/what-is-tensorflow-the-machine-learning-library-explained.html
 * https://www.tensorflow.org/datasets/catalog/mnist
 * https://opencv.org/about/
 * https://pypi.org/project/opencv-python/
 * https://pillow.readthedocs.io/en/stable/
 
