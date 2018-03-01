from flask import Blueprint
from flask import Blueprint, Flask, request, json, jsonify, make_response
from .reviewModel import Reviews, REVIEWS
from ..business.views import BUSINESSES


reviewBlueprint = Blueprint('reviews', __name__)


@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['POST'])
def createReview(id):
    global REVIEWS
    global BUSINESSES
    
    revObj = Reviews('13123112', '23424234', 'Example review')
    jsn = request.data
    data = json.loads(jsn)

    print(BUSINESSES)

    if not BUSINESSES:
        return jsonify({'message':'No Existing Businesses, Register one!'})
    else:        
        for x,y in enumerate(BUSINESSES, 0):
            for key, val in y.items():
                if key == id:
                    print(key)
                    res = revObj.createNewReview(data['id'], id, data['review'])
                    if res:
                        return jsonify({'message':'Review has been Successfully Created.'})
                    else:
                        return jsonify({'message':'Review was not created'})
                else:
                    return jsonify({'message':'No Business Exists with that id'})


@reviewBlueprint.route('/api/businesses/<string:id>/reviews', methods=['GET'])
def getBusReviews(id):
    global REVIEWS

    foundReviews =[]
    if not REVIEWS:
        return jsonify({'message':'No reviews For any business Exst so far!'})
    else:
        for x,y in enumerate(REVIEWS, 0):
            for key, val in y.items():
                if key == id:
                    foundReviews.append(REVIEWS[x])
                    if len(foundReviews) > 0:
                        return jsonify({'Business Reviews':foundReviews})
                    else:
                        return jsonify({'message':'No found Reviews for that business'})
