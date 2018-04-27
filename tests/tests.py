import unittest
# from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
from flask import redirect, jsonify, request, Response, json
from werkzeug.security import generate_password_hash, check_password_hash
from main.views.business.businessModel import Business, BUSINESSES
from main.views.user.userModel import User
from main.views.user.views import SECRETKEY
from main.views.reviews.reviewModel import Reviews
from main import app
# from uuid import uuid4

class TestUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_UserInstance(self):
        self.userObj1 = User(12323231313, 'louis', 'louis@eemail.com', generate_password_hash('password'))
        self.assertIsInstance(self.userObj1, User)        

    def test_user_secret_key(self):
        pass
        global SECRETKEY
        res = 'thisISverysecret'
        self.assertEqual(res, SECRETKEY)

    def test_user_registration_success_message(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louisa", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertEqual('user has been successfully registered.', data['message'])

    def test_user_login_successful(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"id":23243242, "username": "louis", "password": "somepassword", "email": "some@email.com"}))
        self.assertEqual(200, response.status_code)

    def test_user_login_failed(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"id":23243242, "username": "lou", "password": "somepassword", "email": "some@email.com"}))
        self.assertEqual(401, response.status_code)

    def test_user_already_exists_registration(self):
        self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))

        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "anotherperson@email.com"}))

        self.assertEqual(400, response.status_code)
    
    def test_special_characters_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "xxxx!", "password": "somepassword", "email": "some@email.com"}))        
        self.assertEqual(400, response.status_code)

    def test_short_username_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "xxx", "password": "somepassword", "email": "some@email.com"}))        
        self.assertEqual(400, response.status_code)

    def test_missing_username_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"email": "user@email.com", "password": "password"}))
        self.assertEquals(400, response.status_code)

    def test_bad_email_format_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"email": "useremail.com", "password": "password"}))
        self.assertEquals(400, response.status_code)

    def test_missing_email_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "somepassword", "password": "somepassword"}))
        self.assertEquals(400, response.status_code)    
        
    def test_user_fields_createUser(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid":234234232, "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))        
        self.assertTrue(400, response.status_code)

    def test_user_data_length(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid":234234232, "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        self.assertEquals('application/json', response.content_type)

    
        
        
class TestBusiness(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.busObj = Business(1234545543, 'somebusiness', 123132123, 'somelocation', 'somecategory', 'somedescription')
        self.busObj1 = Business(1234534345, 'some', 123132123, 'somelocation', 'somecategory', 'somedescription')
        self.assertIsInstance(self.busObj, Business)

    def test_business_instance(self):
        self.assertIsInstance(self.busObj, Business)
        
    def test_create_business_successful(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"id":234234232, "name": "fsfsf", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))

        self.assertTrue(201, response.status_code)
        
    def test_create_business_failed(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "fsfs", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))

        self.assertTrue(400, response.status_code)

    def test_short_business_name(self):
        pass
        

    def test_delete_business_successful(self):
        # response = self.client.post('/api/v1/auth/register', content_type='application/json',
        #                             data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))

        # response = self.client.put('/api/businesses/123123123', content_type='application/json')
                    
        # self.assertEqual(400, response.status_code)
        pass

    def test_update_business_successful(self):
        # Business.create_business(self.busObj)
        # result = Business.update_business(1231231231)
        # self.assertIsNotNone(result)
        pass

    def test_update_business_failed(self):
        Business.create_business(self.busObj)
        result = Business.update_business(1231)
        self.assertIsNone(result)
    
    

class TestReviewRoutes(unittest.TestCase):

    def setUp(self):
        # self.business = Business.create_business(self.)
        self.revObj = Reviews('12345', '12345', 'this is an example review')
    
    def test_review_instance(self):
        self.assertIsInstance(self.revObj, Reviews)

    def test_create_review_success(self):
        # Business.create_business(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        # review = Reviews.createNewReview(335343454, 1231231231, 'this is a test review')
        # self.assertTrue(review)
        pass

    def test_get_reviews_success(self):
        # Business.create_business(self, 1231231231,'businessName', 435523454, 'kampala', 'tech', 'a technology business')
        # Reviews.createNewReview(335343454, 1231231231, 'this is a test review')
        # result = Reviews.getBizReview(1231231231)
        # self.assertTrue(result)
        pass
    

if __name__ == '__main__':
    unittest.main()