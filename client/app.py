"""Filename: hello-world.py
  """

from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)

@app.route('/users')
def hello_world():
	url = "http://localhost:5000/user" ## server api
	data = json.load(urllib.request.urlopen(url))
	return render_template('index.html',data=data)
	
if __name__ == '__main__':
    app.run(debug=True, port=5001)
	
#This is my client