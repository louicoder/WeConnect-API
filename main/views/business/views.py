from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .businessModel import Business, BUSINESSES
import jwt
import datetime
from functools import wraps
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from ..user.views import loggedInUser, token_required
from flasgger import Swagger, swag_from

businessBlueprint = Blueprint('business', __name__)
loggedInUser= ['773458ufdssdfs908098sdf']

@businessBlueprint.route('/api/businesses', methods=['POST'])
# @token_required
@swag_from('createBusiness.yml')
def createBusiness():
    global BUSINESSES
    global loggedInUser
    
    jsn= request.data
    data = json.loads(jsn)
    
    if len(data.keys()) != 4:
        return jsonify({'message':'some fields are missing, try again'})

    bizname = data['name']
    location = data['location']
    category = data['category']
    
    specialChars = ['@', '#', '$', '%', '^', '&', '*', '!', '(', ')', '/', '?']

    # check business name for special characters
    for x in bizname:
        if x in specialChars:
            return jsonify({'message':'business name contains special characters, try again'})

    # check location for special characters
    for x in location:
        if x in specialChars:
            return jsonify({'message':'location contains special characters, try again'})

    # check category for special characters
    for x in category:
        if x in specialChars:
            return jsonify({'message':'category contains special characters, try again'})

    #create class object for business class 
    busx = Business(str(uuid4()), data['name'], loggedInUser[0], data['location'], data['category'], data['description'])

    if len(bizname) < 5:
        return jsonify({'message':'business name is short, it must be 5 characters and above'}), 400 #bad request
    
    for x in BUSINESSES:
        for k, v in x.items():
            if v[0] == bizname:
                return jsonify({'message':'business with that name already exists, try again'}), 400 #bad request

    # parameters [{businessid:[name, userid, location, category, description]}]
    res = busx.createBusiness(str(uuid4()), data['name'], loggedInUser[0], data['location'], data['category'], data['description'])
    
    if res:
        return jsonify({'message': 'Business successfully created'}), 201 #created
    else:
        return jsonify({'message':'Business was not created, Try again'}), 409 #conflict


@businessBlueprint.route('/api/businesses/<string:id>', methods=['GET'])
# @token_required
@swag_from('retrieveBusiness.yml')
def getOneBusiness(id):
    """ function to retrieve a single business by id"""
    global BUSINESSES
    # bus = Business(1232312, 'name', 'location', 'category', 'description')

    # auth = request.authorization

    # if not auth:
    #     return jsonify({'message':'please login to see businesses'}), 401

    if not BUSINESSES:
        return jsonify({'message':'No records of any Business Exist.'})
    else:
        result = Business.checkBusinessExists(id)
        if result or result == 0:
            return jsonify({'business':BUSINESSES[result]}), 200
        else:
            return jsonify({'business':'No Records of that business Exists'}), 404
    


@businessBlueprint.route('/api/businesses', methods=['GET'])
# @token_required
@swag_from('retrieveAllBusinesses.yml')
def getAllBusinesses():
    """"Function that returns all registered businesses"""
    global BUSINESSES
    if not BUSINESSES:
        return jsonify({'message':'No records found. register a business'}), 404
    else:        
        return jsonify({'Businesses': BUSINESSES}), 200

@businessBlueprint.route('/api/businesses/<string:id>', methods=['PUT'])
# @token_required
@swag_from('updateBusiness.yml')
def updatebusiness(id):
    """Function to update business using the id"""
    global BUSINESSES    
    if BUSINESSES:
        jsn= request.data
        data = json.loads(jsn)
        exists = Business.checkBusinessExists(id)
        busId = ''
        
        if len(data.keys()) != 4:
            return jsonify({'message':'some fields are missing, try again'})
        
        if exists or exists == 0:
            res = BUSINESSES[exists]
            for k, v in res.items():
                busId = k
                BUSINESSES[exists] = {busId : [data['name'], loggedInUser[0], data['location'], data['category'], data['description']]}
                return jsonify({'message':'Business has been updated successfully'}), 200
        else:
            return jsonify({'message': 'no records of that business exists'}), 404

        
@businessBlueprint.route('/api/businesses/<string:id>', methods=['DELETE'])
# @token_required
@swag_from('deleteBusiness.yml')
def deletebusiness(id):
    global BUSINESSES    
    
    if BUSINESSES:
        result = Business.deleteBusiness(id)
        # print(result)
        if result or result == 0:
            BUSINESSES.pop(result)
            return jsonify({'message':'Business has been successfully deleted'}), 200
        else:
            return jsonify({'message':'No business has that id, nothing was deleted.'}), 400
    else:
        return jsonify({'message': 'No records of any Business Exist.'}), 404