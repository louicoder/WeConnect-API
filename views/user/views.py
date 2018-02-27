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
    if not USERS:
        return jsonify({'message':'No users found in the system'})
    else:
        usersx = USERS
        return jsonify({"USERS":usersx})

@userBlueprint.route('/api/v1/auth/login', methods=['POST'])
def login():
    global loggedInUser
    username=request.json['username']
    password=request.json['password']

    if USERS:
        for x in USERS:
            for k in x:
                if x['username'] == username and x['password'] == password:
                    loggedInUser.append({'username':username, 'password':password})
                    return make_response(jsonify({'message':'login successful'})), 200
                else:
                    return make_response(jsonify({'message':'login unsuccessful'})), 401
    else:
        return make_response(jsonify({'message':'No users found in the system.'})), 404

@userBlueprint.route('/api/v1/auth/resetpassword', methods=['PUT'])
def resetPassword():
    global USERS
    global loggedInUser
    username=''
    for x in loggedInUser:
        for y in x:
            username = x['username']

    if not USERS:
        return jsonify({'message': 'no users found in system'})
    else:
        for x in USERS:
            for k in x:
                if x['username'] == username:
                    x['password'] = 'password'
                    print(USERS)
                    return make_response(jsonify({'message':'password Reset successful'})), 200
                else:
                    return make_response(jsonify({'message':'password change was not unsuccessful'})), 401

@userBlueprint.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    global loggedInUser
    if loggedInUser:
        loggedInUser = None
        return jsonify({'message':'You are now logged out'})
    else:
        return make_response(jsonify({'message':'No one logged in so far'}))

@userBlueprint.route('/api/v1/auth/getlogged', methods=['GET'])
def logged():
    global loggedInUser
    if loggedInUser:       
        return jsonify({'loggedInUser':loggedInUser})
    else:
        return make_response(jsonify({'message':'No one logged in so far'}))


