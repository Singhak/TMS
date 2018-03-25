from flask import Flask
from flask_pymongo import PyMongo # Database connector
from bson.objectid import ObjectId # For ObjectId to work
import user.user as usr

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'voiceauth'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/voiceauth'
client = PyMongo(app)    #Configure the connection to the database
# db = client.db.voiceauth
	
@app.route('/adduser', methods=['POST'])
def add_new_user():
	return usr.add_user(client)
	
@app.route('/user', methods=['GET'])
def get_alluser():
	return usr.list_alluser(client)
	
@app.route('/user/<string:name>', methods=['GET'])
def get_oneuser(name):
	print("one user")
	return usr.one_user(name, client)
	
if __name__ == '__main__':
	app.run()
	
## This is my entry point of Db where i calling user related function