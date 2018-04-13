from flask import Blueprint, Flask, request, json, jsonify, make_response
from .userModel import User, USERS
import jwt
import datetime
from functools import wraps
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger, swag_from

loggedInUser=[]
userBlueprint = Blueprint('user', __name__)

SECRETKEY = 'thisISverysecret'
token = None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        data =''
        if not token:
            return jsonify({'message':'token is missing!'}), 403
        try:
            data = jwt.decode(token, SECRETKEY)
        except:
            return jsonify({'message':'Token is invalid'}), 403

        return f(*args, **kwargs)
    return decorated


@userBlueprint.route('/api/v1/auth/register', methods=['POST'])
@swag_from('createUser.yml')
def createuser():
    global USERS
    jsn = request.data
    data= json.loads(jsn)
    if len(data.keys()) != 3:
        return jsonify({'message':'cannot register because of missing fields, check email,username and password'}), 400 #bad request
    
    specialChars = ['@', '#', '$', '%', '^', '&', '*', '!', '(', ')', '/'] #, '(', ')', '?', '/', '\', '-']
    username = data['username']
    for x in username:
        if x in specialChars:
            return jsonify({'message':'username contains special characters, try again'}), 400 #bad request

    # usernames=[]
    # print(USERS)
    for x in USERS:
        for k, v in x.items():
            if v == data['username']:            
                return jsonify({'message':'user already exists'}), 400 #bad request
    

    if data['username'] and data['email'] and data['password'] and len(data['username']):
        username = data['username']
        email = data['email']
        password = data['password']
        password = generate_password_hash(password)            
        USERS.append({"userid":str(uuid4()), "username":username, "email":email, "password":password})
        print(USERS)
        return jsonify({"message":"User has been Successfully registered."}), 200

@userBlueprint.route('/api/v1/auth/getusers', methods=['GET'])
# @token_required
def getusers():
    global USERS    
    if not USERS:
        return jsonify({'message':'No users found in the system'})
    else:
        usersx = USERS
        return jsonify({"USERS":usersx})
    

@userBlueprint.route('/api/v1/auth/login', methods=['POST'])
@swag_from('loginUser.yml')
def login():

    auth = request.authorization

    if auth:
        username=auth.username
        password=auth.password
        token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)
        
        if USERS:
            
            for x in USERS:
                for k in x:
                    if x['username'] == username and check_password_hash(x['password'], password):
                        loggedInUser.append([x['userid'], x['username']])                  
                        return jsonify({'token': token.decode('UTF-8')}), 200                      
                    else:                        
                        return jsonify({'message':'unauthorised access'}), 401
        else:
            return make_response(jsonify({'message':'No users found in the system'})), 404
    else:
        return jsonify({"message":"Could not verify authetication"})
        
    return make_response(jsonify({'message':'couldnt verify'})), 401
    

@userBlueprint.route('/api/v1/auth/resetpassword', methods=['PUT'])
# @token_required
@swag_from('resetUserPassword.yml')
def resetPassword():
    global USERS
    global loggedInUser
    
    if len(loggedInUser) == 0:
        return jsonify({"message":"please first login"}), 401

    for x in loggedInUser:
        for y in x:
            username = x['username']

    if not USERS:
        return jsonify({'message': 'no users found in system'}), 404
    else:
        for x in USERS:
            for k in x:
                if x['username'] == username:
                    x['password'] = 'password'
                    print(USERS)
                    return jsonify({'message':'password Reset successful'}), 200
                else:
                    return jsonify({'message':'password change was not successful'}), 400

@userBlueprint.route('/api/v1/auth/logout', methods=['POST'])
# @token_required
@swag_from('logoutUser.yml')
def logout():
    global loggedInUser
    global USERS
    request.authorization = None
    # del USERS[:]
    del loggedInUser[:]

    if not request.authorization:        
        return jsonify({'message':'you have successfully logged out'}), 200
    else:        
        return jsonify({'message':'something went wrong, please try again'}), 400
    



