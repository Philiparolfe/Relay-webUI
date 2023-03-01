from flask import Flask, request, render_template

from relay_module import switchOn,switchOff, is_on
app = Flask(__name__)

@app.route('/')
def home():
    status = [
        is_on(0),
        is_on(1),
        is_on(2),
        is_on(3),
    ]
    color = 'green'
    return render_template('index.html', isLit=status, color=color)

@app.route('/on/<num>')
def on(num):
    switchOn(int(num))
    return home()

@app.route('/off/<num>')
def off(num):
    switchOff(int(num))
    return home()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
