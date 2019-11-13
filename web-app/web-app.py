# Richard Cooke
# G00331787

# Flask web app to that reads the data in the static html page and passes it to the model in the jupyter notebook

# Importing flask
import flask as fl

app = fl.Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('web-app.html')

app.run()