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
    bus = Business(1232312, request.json['name'], request.json['location'], request.json['category'], request.json['description'])
    res = bus.createBusiness(123321, request.json['name'], request.json['location'], request.json['category'], request.json['description'])

    if res:
        return jsonify({'message': 'Business successfully created'})
    else:
        return jsonify({'message':'Business was not created, Try again!!'})
       

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
    bus = Business(1232312, request.json['name'], request.json['location'], request.json['category'], request.json['description'])
    if BUSINESSES:
        res = bus.updateBusiness(request.json['id'], request.json['name'], request.json['location'], request.json['category'], request.json['description'])
        print(res)
        if res:
            return jsonify({'message':'Business Updated Sucessfully'})
        else:
            return jsonify({'message':'Business was not updated'})
        
