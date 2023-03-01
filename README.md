# Relay Control WebUI
This document provides a brief documentation for the HTML code snippet given above. This code snippet includes a table of four relays with their ON and OFF buttons.
# Flask App Documentation
This is a Flask app that controls relays using the relay_module.

Installation
Install Python 3 if not already installed
Install Flask using pip install flask
Usage
Import the necessary functions from relay_module
Create a Flask app instance with Flask(__name__)
Define routes using @app.route()
Define functions to be executed when a route is accessed
Run the app using app.run()
Functions
home()
Returns the index.html template when the / route is accessed.

on(num)
Turns on the relay specified by num using the switchOn() function from relay_module.

off(num)
Turns off the relay specified by num using the switchOff() function from relay_module.

Example
python
Copy code
from flask import Flask, request, render_template
from relay_module import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/on/<num>')
def on(num):
    switchOn(int(num))
    return home()

@app.route('/off/<num>')
def off(num):
    switchOff(int(num))
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
This example creates a Flask app instance, defines routes for turning on and off relays, and runs the app on localhost port 5000.
