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

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):        
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#         data =''
#         if not token:
#             return jsonify({'message':'token is missing!'}), 403
#         try:
#             data = jwt.decode(token, SECRETKEY)
#         except:
#             return jsonify({'message':'Token is invalid'}), 403

#         return f(*args, **kwargs)
#     return decorated


@userBlueprint.route('/api/v1/auth/register', methods=['POST'])
@swag_from('createUser.yml')
def createuser():
    global USERS
    jsn = request.data
    data= json.loads(jsn)
    # if len(data.keys()) != 3:
    #     return jsonify({'message':'cannot register because of missing fields, check email,username and password'}), 400 #bad request
    
    specialChars = ['@', '#', '$', '%', '^', '&', '*', '!', '/', '?', '-', '_']
    
    # check that username is not missing
    if 'username' not in data.keys():
        return jsonify({'message':'username is missing'}), 400 #bad request
    else:
        username = data['username']

    #check that email is not missing
    if 'email' not in data.keys():
        return jsonify({'message':'email is missing'}), 400 #bad request
    else:
        email = data['email']

    #check that password is not missing
    if 'password' not in data.keys():
        return jsonify({'message':'password is missing'}), 400 #bad request
    else:
        password = data['password']

    #check whether username contains special characters, its forbidden!
    for x in username:
        if x in specialChars:
            return jsonify({'message':'username contains special characters'}), 400 #bad request

    #check length of username, should be five characters and above
    if len(username) < 5:
        return jsonify({'message':'username should be five characters and above'}), 400 #bad request

    if len(data['password']) < 5:
        return jsonify({'message':'password should be five characters and above'}), 400 #bad request

    #check if the email contains a dot
    if '.' not in data['email']:
        return jsonify({'message':'email is invalid, dot missing'}), 400 #bad request

    #check if the email contains an @ symbol
    if '@' not in data['email']:
        return jsonify({'message':'email is invalid, @ missing'}), 400 #bad request
    
    #check whether username has already been taken.
    for x in USERS:
        for k, v in x.items():
            if v == username:            
                return jsonify({'message':'user already exists'}), 400 #bad request
    
    password = generate_password_hash(password)            
    USERS.append({"userid":str(uuid4()), "username":username, "email":email, "password":password})
    return jsonify({"message":"user has been successfully registered."}), 201 #created

# @userBlueprint.route('/api/v1/auth/getusers', methods=['GET'])
# def getusers():
#     global USERS    
#     if not USERS:
#         return jsonify({'message':'No users found in the system'})
#     else:
#         usersx = USERS
#         return jsonify({"USERS":usersx})
    

@userBlueprint.route('/api/v1/auth/login', methods=['POST'])
@swag_from('loginUser.yml')
def login():
    global loggedInUser
    global USERS
    auth = request.authorization
    
    jsn = request.data
    data= json.loads(jsn)

    if loggedInUser:        
        return jsonify({'message':'you are already logged in'}), 400 #bad request
    
    if not USERS:
        return jsonify({'message':'you are not yet registered'}), 401 # unauthorized access
    
    if auth:
        username=auth.username
        password=auth.password
        token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)
        
        if USERS:            
            for x in USERS:
                for k in x:
                    if x['username'] == username and check_password_hash(x['password'], password):
                        loggedInUser.append([x['userid'], x['username']])                  
                        return jsonify({'token': token.decode('UTF-8'), 'message':'logged in successfully'}), 200
                        # return jsonify({'message':'Logged in Successfully'}), 200
                    else:                        
                        return jsonify({'message':'unauthorised access, wrong username or password'}), 401
    elif data:
        username=data['username']
        password=data['password']
        # token = jwt.encode({'user':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)
        
        if USERS:            
            for x in USERS:
                for k in x:
                    if x['username'] == username and check_password_hash(x['password'], password):
                        loggedInUser.append([x['userid'], x['username']])                  
                        # return jsonify({'token': token.decode('UTF-8'), 'message':'logged in successfully'}), 200
                        return jsonify({'message':'logged in successfully'}), 200
                    else:                        
                        return jsonify({'message':'unauthorised access, wrong username or password'}), 401 # unauthorised access
    
    else:
        return jsonify({"message":"Could not verify authetication"}), 401  # unauthorised access
        
    return make_response(jsonify({'message':'couldn''t verify login'})), 401 # unauthorised access
    

@userBlueprint.route('/api/v1/auth/resetpassword', methods=['PUT'])
# @swag_from('resetUserPassword.yml')
def resetPassword():
    global USERS
    global loggedInUser
    

    #check that we have users registered
    if not USERS:
        return jsonify({"message":"no users found, first register"}), 404 # not found

    #check if user is already logged in
    if len(loggedInUser) == 0:
        return jsonify({"message":"please first login"}), 401 # unauthorized access   

    for x in loggedInUser:
        for y in x:
            username = x['username']

   

    for x in USERS:
        for k in x:
            if x['username'] == username:
                x['password'] = 'password'
                print(USERS)
                return jsonify({'message':'password was reset successfully'}), 200
            else:
                return jsonify({'message':'password reset was not successful'}), 400

@userBlueprint.route('/api/v1/auth/logout', methods=['POST'])
@swag_from('logoutUser.yml')
def logout():
    global loggedInUser
    global USERS   

    if not loggedInUser:
        return jsonify({'message':'you are already logged out'}), 400 #bad request

    if len(loggedInUser) > 0:
        del loggedInUser[:]
        request.authorization = None
        return jsonify({'message':'you have successfully logged out'}), 200 #ok
    else:        
        return jsonify({'message':'something went wrong, please try again'}), 400 #bad request
    
