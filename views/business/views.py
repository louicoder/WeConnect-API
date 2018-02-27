from flask import Blueprint
import random

businessBlueprint = Blueprint('business', __name__)

businessList=[]
# @businessBlueprint.route('/api/v1/auth/createBusiness')
# def createBusiness():
#     global businessList    
#     businessList.append({})
#     return 