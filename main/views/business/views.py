from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .businessModel import Business, BUSINESSES
import jwt
import datetime
from functools import wraps
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from ..user.views import loggedInUser
from flasgger import Swagger, swag_from

businessBlueprint = Blueprint('business', __name__)
# loggedInUser= ['773458ufdssdfs908098sdf']

@businessBlueprint.route('/api/businesses', methods=['POST'])
@swag_from('createBusiness.yml')
def create_business():
    global BUSINESSES
    global loggedInUser

    if len(loggedInUser) == 0:
        return jsonify({'message':'please login to register business'}), 401 # unauthorized access
    
    jsn= request.data
    data = json.loads(jsn)
    
    if len(data.keys()) != 4:
        return jsonify({'message':'some fields are missing, try again'}), 400 #bad request
    
    if 'name' not in data.keys():
        return jsonify({'message':'name is missing'}), 400 #bad request

    if 'location' not in data.keys():
        return jsonify({'message':'location is missing'}), 400 #bad request

    if 'category' not in data.keys():
        return jsonify({'message':'category is missing'}), 400 #bad request

    if 'description' not in data.keys():
        return jsonify({'message':'description is missing'}), 400 #bad request

    if len(data['name']) < 5:
        return jsonify({'message':'name of business should be five characters and above'}), 400 #bad request


    bizname = data['name']
    location = data['location']
    category = data['category']
    
    # list special characters to be checked for in strings
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

    #check length of business name.
    if len(bizname) < 5:
        return jsonify({'message':'business name is short, it must be five characters and above'}), 400 #bad request
    
    for x in BUSINESSES:
        for k, v in x.items():
            if v[0] == bizname:
                return jsonify({'message':'business with that name already exists, try again'}), 400 #bad request
    

    #create class object for business class 
    busx = Business(str(uuid4()), data['name'], loggedInUser[0], data['location'], data['category'], data['description'])

    # parameters [{businessid:[name, userid, location, category, description]}]
    res = busx.create_business()
    
    if res:
        return jsonify({'message': 'Business successfully created'}), 201 #created
    else:
        return jsonify({'message':'Business was not created, Try again'}), 409 #conflict


@businessBlueprint.route('/api/businesses/<string:id>', methods=['GET'])
@swag_from('retrieveBusiness.yml')
def get_one_business(id):
    """ function to retrieve a single business by id"""
    global BUSINESSES    

    if not BUSINESSES:
        return jsonify({'message':'no records of any business exist.'}), 404 #not found
    else:
        result = Business.get_one_business(id)
        if result or result == 0:
            return jsonify({'business':BUSINESSES[result]}), 200 #ok
        else:
            return jsonify({'business':'no records of that business exist'}), 400 #bad request
    

@businessBlueprint.route('/api/businesses', methods=['GET'])
@swag_from('retrieveAllBusinesses.yml')
def get_all_businesses():
    """"Function that returns all registered businesses"""
    global BUSINESSES
    if not BUSINESSES:
        return jsonify({'message':'No records found. register a business'}), 404 #not found
    else:        
        return jsonify({'Businesses': BUSINESSES}), 200


@businessBlueprint.route('/api/businesses/<string:id>', methods=['PUT'])
@swag_from('updateBusiness.yml')
def update_business(id):
    """Function to update business using the id passed from parameter"""
    global BUSINESSES
    global loggedInUser

    if len(loggedInUser) == 0:
        return jsonify({'message':'you are logged out, please login'}), 401 #anauthorized access

    if BUSINESSES:
        jsn= request.data
        data = json.loads(jsn)
        exists = Business.get_one_business(id)
        busId = ''
        
        if len(data.keys()) != 4:
            return jsonify({'message':'some fields are missing, try again'}), 400 #bad request

        if data['name']:
            name = data['name']
        else:
            name = ''

        if data['location']:
            location = data['location']
        else:
            location = ''

        if data['category']:
            category = data['category']
        else:
            category = ''
        
        if data['description']:
            description = data['description']
        else:
            description = ''
        
        if exists or exists == 0:
            res = BUSINESSES[exists]
            for k, v in res.items():
                busId = k
                BUSINESSES[exists] = {busId : [name, loggedInUser[0], location, category, description]}
                return jsonify({'message':'Business has been updated successfully'}), 200 #ok
        else:
            return jsonify({'message': 'no records of that business exist'}), 404 #not found

        
@businessBlueprint.route('/api/businesses/<string:id>', methods=['DELETE'])
@swag_from('deleteBusiness.yml')
def delete_business(id):
    """Function is responsible for deleting a business ased on parameter passed as id"""
    global BUSINESSES    
    
    if BUSINESSES:
        result = Business.delete_business(id)
        # print(result)
        if result or result == 0:
            BUSINESSES.pop(result)
            return jsonify({'message':'business has been successfully deleted'}), 200 #ok
        else:
            return jsonify({'message':'No business has that id, nothing was deleted'}), 400 #bad request
    else:
        return jsonify({'message': 'No records of any Business Exist'}), 404 #not found