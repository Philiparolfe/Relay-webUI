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
