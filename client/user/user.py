"""Filename: hello-world.py
  """

from flask import Flask
import json
import urllib.request

app = Flask(__name__)

@app.route('/users')
def hello_world():
	url = "http://localhost:5000/user/anil"
	data = json.load(urllib.request.urlopen(url))
	return("Hello {}!".format(data))
	
if __name__ == '__main__':
    app.run(debug=True, port=5001)
	