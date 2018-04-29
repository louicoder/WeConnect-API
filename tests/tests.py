import unittest
# from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
from flask import redirect, jsonify, request, Response, json
from werkzeug.security import generate_password_hash, check_password_hash
from main.views.business.businessModel import Business, BUSINESSES
from main.views.user.userModel import User
from main.views.user.views import SECRETKEY
from main.views.reviews.reviewModel import Reviews
from main import app
from main.views.user.views import loggedInUser
from main.views.user.views import USERS

# from uuid import uuid4

class TestUser(unittest.TestCase):

    # def __init__():
    #     tear_down()
    @staticmethod
    def tear_down():
        global loggedInUser
        global USERS
        del loggedInUser[:]
        del USERS[:]

    def setUp(self):
        self.client = app.test_client()
        self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))

    def test_UserInstance(self):
        self.userObj1 = User(12323231313, 'louis', 'louis@eemail.com', generate_password_hash('password'))
        self.assertIsInstance(self.userObj1, User)

    def test_user_secret_key(self):
        pass
        global SECRETKEY
        res = 'thisISverysecret'
        self.assertEqual(res, SECRETKEY)

    def test_user_registration_success(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louisa", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertEqual(201, response.status_code)
        self.assertEqual('user has been successfully registered.', data['message'])

    def test_user_already_exists_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "anotherperson@email.com"}))
        data = json.loads(response.data)
        self.assertEqual('user already exists', data['message'])
        self.assertEqual(400, response.status_code)
    
    def test_special_characters_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "xxxx!", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('username contains special characters', data['message'])

    def test_short_username_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "xxx", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('username should be five characters and above', data['message'])

    def test_missing_username_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"email": "user@email.com", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('username is missing', data['message'])

    def test_bad_email_format_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username":"personx", "email": "useremail.com", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('email is invalid, @ symbol missing', data['message'])

    def test_missing_email_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "somepassword", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual(400, response.status_code)
        self.assertEqual('email is missing', data['message'])
        
    def test_data_keys_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid":234234232, "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        data = json.loads(response.data)
        self.assertTrue(400, response.status_code)
        self.assertNotEqual(4, data.keys())


    def test_user_data_type(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        self.assertEqual('application/json', response.content_type)    

    def test_user_login_failed_wrong_username(self):        
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "lou", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual('unauthorised access, wrong username or password', data['message'])        
        self.assertEqual(401, response.status_code)

    def test_user_login_failed_wrong_password(self):        
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "password"}))
        data = json.loads(response.data)
        self.assertIn('unauthorised access, wrong username or password', data['message'])        
        self.assertEqual(401, response.status_code)

    def test_user_login_successful(self):
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword"}))
        data = json.loads(response.data)
        self.assertEqual('logged in successfully', data['message'])
        self.assertEqual(200, response.status_code)

    def test_already_loggedin_user(self):
        # self.client.post('/api/v1/auth/login', content_type='application/json',
        #                             data=json.dumps({"username": "louis", "password": "somepassword"}))
        response = self.client.post('/api/v1/auth/login', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "password"}))
        data = json.loads(response.data)
        self.assertEqual(401, response.status_code)
        self.assertEqual('unauthorised access, wrong username or password', data['message'])

TestUser.tear_down()
        
        
class TestBusiness(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.busObj = Business(1234545543, 'somebusiness', 123132123, 'somelocation', 'somecategory', 'somedescription')

        self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username": "louis", "password": "somepassword", "email": "some@email.com"}))

        self.client.post('/api/v1/auth/login', content_type='application/json',
                            data=json.dumps({"username": "louis", "password": "somepassword"}))


    def test_business_instance(self):
        self.assertIsInstance(self.busObj, Business)

    def test_create_business_successful(self):        
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "nameofbusiness", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business successfully created', data['message'])
        self.assertTrue(400, response.status_code)
        
    def test_business_already_exists(self):        
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "somebusiness", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business successfully created', data['message'])
        self.assertTrue(201, response.status_code)        
        
    def test_short_name_create_business(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "fsf", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('name of business should be five characters and above', data['message'])
        self.assertEqual(400, response.status_code)

    def test_name_missing_create_business(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"location": "kampala", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business name is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_location_missing_create_business(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "fsf", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('location is missing', data['message'])
        self.assertEqual(400, response.status_code)
    
    def test_category_missing_create_business(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "fsf", "location": "kampala", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('category is missing', data['message'])
        self.assertEqual(400, response.status_code)

    def test_description_missing_create_business(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name": "fsf", "location": "kampala", "category": "somecategory"}))
        data = json.loads(response.data)
        self.assertEqual('description is missing', data['message'])
        self.assertEqual(400, response.status_code)        

    def test_delete_business_failed(self):
        response = self.client.delete('/api/businesses/123123123', content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual('No business has that id, nothing was deleted', data['message'])
        self.assertEqual(400, response.status_code)

    def test_business_name_with_special_characters(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name":"business!", "location": "kampala", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business name contains special characters, try again', data['message'])
        self.assertEqual(400, response.status_code)

    def test_business_location_with_special_characters(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name":"business", "location": "kampala!", "category": "somecategory", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business location contains special characters, try again', data['message'])
        self.assertEqual(400, response.status_code)

    def test_business_category_with_special_characters(self):
        response = self.client.post('/api/businesses', content_type='application/json',
                                    data=json.dumps({"name":"business", "location": "kampala", "category": "somecategory!", "description":"some description for the business"}))
        data = json.loads(response.data)
        self.assertEqual('business category contains special characters, try again', data['message'])
        self.assertEqual(400, response.status_code)

    
        

    def test_update_business_successful(self):
        # Business.create_business(self.busObj)
        # result = Business.update_business(1231231231)
        # self.assertIsNotNone(result)
        pass

    def test_update_business_failed(self):
        response = self.client.put('/api/businesses')
        
    
    

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