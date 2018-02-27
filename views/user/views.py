from flask import Blueprint, Flask, request, json, jsonify, make_response
import random
from models import User, USERS

userBlueprint = Blueprint('user', __name__)

@userBlueprint.route('/api/v1/auth/register', methods=['POST'])
def createuser():
    global USERS
    
    # userx = User(random.randint(1, 100000000), request.json['username'], request.json['email'], request.json['password'])
    # userx = [{"userid":random.randint(1, 100000000), "username":username, "email":email, "password":password}]
    userid = random.randint(1, 100000)
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']       
    USERS.append({"userid":userid, "username":username, "email":email, "password":password})    
    return jsonify({"users":USERS})
    

@userBlueprint.route('/api/v1/auth/getusers', methods=['GET'])
def getusers():
    global USERS
    usersx = USERS
    return jsonify({"USERS":usersx})



