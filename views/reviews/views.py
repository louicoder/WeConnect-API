from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .reviewModel import Reviews, REVIEWS
from ..business.views import BUSINESSES
from uuid import uuid4
from flasgger import Swagger, swag_from
from ..user.views import loggedInUser, token_required

reviewBlueprint = Blueprint('reviews', __name__)


@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['POST'])
@swag_from('createReview.yml')
# @token_required
def createReview(id):
    global REVIEWS
    global BUSINESSES
    
    # revObj = Reviews('13123112', '23424234', 'Example review')
    jsn = request.data
    data = json.loads(jsn)

    print(BUSINESSES)

    if not BUSINESSES:
        return jsonify({'message':'No Existing Businesses, Register one!'})
    else:
        
        for x,y in enumerate(BUSINESSES, 0):
            for key, val in y.items():
                if key == id:
                    revObj = Reviews(str(uuid4()), id, data['review'])
                    res = revObj.createNewReview(str(uuid4()), id, data['review'])
                    if res:
                        return jsonify({'message':'Review has been Successfully Created.', 'review':REVIEWS}), 201
                    else:
                        return jsonify({'message':'Review was not created'}), 403
                else:
                    return jsonify({'message':'No Business Exists with that id'}), 404


@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['GET'])
@swag_from('retrieveReviews.yml')
# @token_required
def getBusReviews(id):
    global REVIEWS
    id = id
    if not REVIEWS:
        return jsonify({'message':'No reviews For any business Exist so far!'})
    else:
        res = Reviews.getBizReview(id)
        print(res)
        if not res:
            return jsonify({'message': 'no review found for that business'}), 409 #Conflict
        else:
            return jsonify({'reviews': res}), 200
        
