import unittest
from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
from werkzeug.security import generate_password_hash, check_password_hash
from ..main.views.business.businessModel import Business, BUSINESSES
from ..main.views.user.userModel import User
from ..main.views.user.views import SECRETKEY
from ..main.views.reviews.reviewModel import Reviews
from ..main import app
from uuid import uuid4




class Test_User_Routes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_UserInstance(self):
        userObj1 = User(12323231313, 'louis', 'louis@eemail.com', generate_password_hash('password'))
        self.assertIsInstance(userObj1, User)        

    def test_user_secret_key(self):
        pass
        global SECRETKEY
        res = 'thisISverysecret'
        self.assertEqual(res, SECRETKEY)
    
    def test_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        
        self.assertEqual(200, response.status_code)
        # self.assertEqual('User has been Successfully registered.', response_data['message'])
        
    def test_user_fields_createUser(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid":str(uuid4()), "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        
        self.assertTrue(400, response.status_code)

    def test_user_missing_fields_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"password": "somepassword", "email": "some@email.com"}))

        self.assertTrue(400, response.status_code)
        
        
class Test_Business_Routes(unittest.TestCase):

    def setUp(self):
        # self.client = app.test_client()
        self.busObj = Business('12345', 'somebusiness',123132123, 'somelocation', 'somecategory', 'somedescription')
        self.assertIsInstance(self.busObj, Business)

    def test_business_instance(self):
        self.assertIsInstance(self.busObj, Business)
        
    def test_create_business(self):        
        business = Business(1231231231, 'someBusiness', 435523454, 'kampala', 'tech', 'a technology business')
        self.assertTrue(business)       
        
    def test_delete_business_success(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        result = Business.deleteBusiness(1231231231)
        self.assertIsNotNone(result)

    def test_delete_business_failed(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        result = Business.deleteBusiness(1231)
        self.assertIsNone(result)

    def test_update_business_successful(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        result = Business.updateBusiness(1231231231)
        self.assertIsNotNone(result)

    def test_update_business_failed(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        result = Business.updateBusiness(1231)
        self.assertIsNone(result)

class Test_Review_Routes(unittest.TestCase):

    def setUp(self):
        self.business = Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        self.revObj = Reviews('12345', '12345', 'this is an example review')
    
    def test_review_instance(self):
        self.assertIsInstance(self.revObj, Reviews)

    def test_create_review_success(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        review = Reviews.createNewReview(335343454, 1231231231, 'this is a test review')
        self.assertTrue(review)

    def test_get_reviews_success(self):
        Business.createBusiness(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        Reviews.createNewReview(335343454, 1231231231, 'this is a test review')
        result = Reviews.getBizReview(1231231231)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()