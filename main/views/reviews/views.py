from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .reviewModel import Reviews, REVIEWS
from ..business.views import BUSINESSES
from uuid import uuid4
from flasgger import Swagger, swag_from
from ..user.views import loggedInUser

reviewBlueprint = Blueprint('reviews', __name__)

@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['POST'])
@swag_from('createReview.yml')
def create_review(id):
    """Function for creating a review for a business whose id is passed as a parameter"""
    global REVIEWS
    global BUSINESSES
    found = [] #found business id matching passed one will be stored in this list
    
    jsn = request.data
    data = json.loads(jsn)    

    if 'review' not in data.keys():
        return jsonify({"message":"review is missing"}), 400 #bad request

    if data.keys() == 0:
        return jsonify({"message":"fields are missing"}), 400 #bad request

    if not BUSINESSES:
        return jsonify({'message':'no businesses exist'}), 404 #not found    

    for x in BUSINESSES:
        for k in x.keys():
            if id == k:
                found.append(k)

    #in case the business id matches any of the registered business ids.
    if found:
        revObj = Reviews(str(uuid4()), id, data['review'])
        res = revObj.create_review(str(uuid4()), id, data['review'])
        if res:
            return jsonify({'message':'review has been successfully created'}), 201 #created
        else:
            return jsonify({'message':'review was not created'}), 400 #bad request
            
    return jsonify({'message':'no business with that id exists'}), 400 #bad request


@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['GET'])
@swag_from('retrieveReviews.yml')
def get_business_reviews(id):
    """Function for retrieving reviews of business whose id is passed as a parameter"""
    global REVIEWS
    business_id = id
    if not REVIEWS:
        return jsonify({'message':'no reviews of any business exist'}), 404 #not found
    else:
        result = Reviews.get_business_reviews(business_id)       
        if not result:
            return jsonify({'message': 'no review found for that business id'}), 400 #bad request
        else:
            return jsonify({'reviews': result}), 200
        
