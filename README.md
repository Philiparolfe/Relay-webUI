# Relay Control WebUI
This document provides a brief documentation for the HTML code snippet given above. This code snippet includes a table of four relays with their ON and OFF buttons.
# Flask App Documentation
This is a Flask app that controls relays using the relay_module.

<h2>Installation</h2>
<ol>
  <li>Install Python 3 if not already installed</li>
  <li>Install Flask using <code>pip install flask</code></li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Import the necessary functions from <code>relay_module</code></li>
  <li>Create a Flask app instance with <code>Flask(name)</code></li>
  <li>Define routes using <code>@app.route()</code></li>
  <li>Define functions to be executed when a route is accessed</li>
  <li>Run the app using <code>app.run()</code></li>
</ol>

<h2>Functions</h2>
<ul>
  <li><code>home()</code>: Returns the <code>index.html</code> template when the <code>/</code> route is accessed.</li>
  <li><code>on(num)</code>: Turns on the relay specified by <code>num</code> using the <code>switchOn()</code> function from <code>relay_module</code>.</li>
  <li><code>off(num)</code>: Turns off the relay specified by <code>num</code> using the <code>switchOff()</code> function from <code>relay_module</code>.</li>
</ul>

<h2>Example</h2>
<pre><code class="python">from flask import Flask, request, render_template
from relay_module import *

app = Flask(name)

@app.route('/')
def home():
return render_template('index.html')

@app.route('/on/')
def on(num):
switchOn(int(num))
return home()

@app.route('/off/')
def off(num):
switchOff(int(num))
return home()

if name == 'main':
app.run(host='0.0.0.0')</code></pre>

<p>This example creates a Flask app instance, defines routes for turning on and off relays, and runs the app on localhost port 5000.</p>

