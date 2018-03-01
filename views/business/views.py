from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .businessModel import Business, BUSINESSES
import jwt
import datetime
from functools import wraps
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

businessBlueprint = Blueprint('business', __name__)

@businessBlueprint.route('/api/v1/auth/businesses', methods=['POST'])
def createBusiness():
    global BUSINESSES
    bus = Business(1232312, 'name', 'location', 'category', 'description')
    jsn= request.data
    data = json.loads(jsn)
    res = bus.createBusiness(data['id'], data['name'], data['location'], data['category'], data['description'])
    # res = bus.createBusiness = {12:['cmopany', 'locatioon', 'category', 'description']}
    
    if res:
        return jsonify({'message': 'Business successfully created'})
    else:
        return jsonify({'message':'Business was not created, Try again!!'})


@businessBlueprint.route('/api/v1/auth/businesses/<string:id>', methods=['GET'])
def getOneBusiness(id):
    global BUSINESSES
    bus = Business(1232312, 'name', 'location', 'category', 'description')

    if not BUSINESSES:
        return jsonify({'message':'No records of any Business Exist.'})
    else:
        result = bus.checkBusinessExists(id)
        if result or result == 0:
            return jsonify({'business':BUSINESSES[result]})
        else:
            return jsonify({'business':'No Records of that business Exists'})



@businessBlueprint.route('/api/v1/auth/businesses', methods=['GET'])
def getAllBusinesses():
    global BUSINESSES
    if not BUSINESSES:
        return jsonify({'message':'No records found. Register a business'})
    else:        
        return jsonify({'Businesses': BUSINESSES})

@businessBlueprint.route('/api/v1/auth/businesses/<string:id>', methods=['PUT'])
def updatebusiness(id):
    global BUSINESSES
    bus = Business(1232312, 'name', 'location', 'category', 'description')
    if BUSINESSES:
        jsn= request.data
        data = json.loads(jsn)
        res = bus.updateBusiness(id)
        print(res)        
        
        if res or res == 0:
            BUSINESSES[res] = {data['id']:[data['name'], data['location'], data['category'], data['description']]}
            return jsonify({'message':'Business Updated Sucessfully'})
        else:
            return jsonify({'message':'Business was not updated'})


        
@businessBlueprint.route('/api/v1/auth/businesses/<string:id>', methods=['DELETE'])
def deletebusiness(id):
    global BUSINESSES    

    if BUSINESSES:
        res = Business(1232312, 'name', 'location', 'category', 'description')
        result = res.deleteBusiness(id)
        print(result)
        if result or result == 0:
            BUSINESSES.pop(result)
            return jsonify({'message':'Business has been successfully deleted'})
        else:
            return jsonify({'message':'No business has that id.'})
    else:
        return jsonify({'message': 'No records of any Business Exist.'})