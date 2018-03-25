from flask import request
from flask import jsonify

def add_user(client):
	# print("Adding new user in db")
	user = client.db.user
	name = request.json['name']
	age = request.json['age']
	user_id = user.insert({'name': name, 'age': age})
	new_user = user.find_one({'_id': user_id })
	output = {'name' : new_user['name'], 'age' : new_user['age']}
	return jsonify({'result' : output})
	
def list_alluser(client):
  user = client.db.user
  output = []
  for s in user.find():
    output.append({'name' : s['name'], 'age' : s['age']})
  return jsonify({'result' : output})
  
def one_user(name, client):
	print(name)
	user = client.db.user
	s = user.find_one({'name' : name})
	if s:
		output = {'name' : s['name'], 'age' : s['age']}
	else:
		output = "No such name"
	return jsonify({'result' : output})
	
## This is my user relate function