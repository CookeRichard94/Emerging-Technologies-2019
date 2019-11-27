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

### 3.3 Tensorflow

### 3.4 MNIST

### 3.5 OpenCV

### 3.6 Other

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
 *
 *
 *
 *
 *
 *
 *
 *
 * https://pypi.org/project/opencv-python/
