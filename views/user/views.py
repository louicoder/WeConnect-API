from flask import Blueprint, Flask, request, json, jsonify, make_response
from .userModel import User, USERS
import jwt
import datetime
from functools import wraps
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

loggedInUser=[]
userBlueprint = Blueprint('user', __name__)

SECRETKEY = 'thisISverysecret'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        data =''
        if not token:
            return jsonify({'message':'token is missing!'}), 403
        try:
            data = jwt.decode(token, SECRETKEY)
        except:
            return make_response(jsonify({'message':'Token is invalid'})), 403

        return f(*args, **kwargs)
    return decorated


@userBlueprint.route('/api/v1/auth/register', methods=['POST'])
def createuser():
    global USERS    
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    password = generate_password_hash(password)
    USERS.append({"userid":str(uuid4()), "username":username, "email":email, "password":password})    
    return jsonify({"users":USERS})
    

@userBlueprint.route('/api/v1/auth/getusers', methods=['GET'])
@token_required
def getusers():
    global USERS
    
    if not USERS:
        return jsonify({'message':'No users found in the system'})
    else:
        usersx = USERS
        return jsonify({"USERS":usersx})
    

@userBlueprint.route('/api/v1/auth/login', methods=['POST'])
def login():

    auth = request.authorization
    username=auth.username
    password=auth.password

    if auth:
        token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)
        print(token)
        if USERS:
            
            for x in USERS:
                for k in x:
                    if x['username'] == username and check_password_hash(x['password'], password):
                        loggedInUser.append({'id':x['userid'], 'username':x['username']})
                        return make_response(jsonify({'message':'login successful'})), 200
                    else:
                        print('here')
                        print(USERS)
                        print(password)
                        return make_response(jsonify({'message':'login unsuccessful'})), 401
        else:
            return make_response(jsonify({'message':'No users found in the system.'})), 404

        return jsonify({'token': token.decode('UTF-8')})

    return make_response(jsonify({'message':'couldnt verify'})), 401
    

@userBlueprint.route('/api/v1/auth/resetpassword', methods=['POST'])
@token_required
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
                    return make_response(jsonify({'message':'password change was not successful'})), 401

@userBlueprint.route('/api/v1/auth/logout', methods=['PUT'])
@token_required
def logout():
    global loggedInUser
    token = request.args.get('token')
    try:
        payload = jwt.decode(token, SECRETKEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return jsonify({'message':'Signature expired. Please log in again.'})
    except jwt.InvalidTokenError:
        return jsonify({'message':'Invalid token. Please log in again.'})




