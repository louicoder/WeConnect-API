import unittest
from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
# from views.business.businessModel import Business
# from views.user.userModel import User
# from ..views.user.views import
from werkzeug.security import generate_password_hash, check_password_hash
from ..views.business.businessModel import Business
from ..view.user.userModel import User
from ..views.reviews.reviewModel import Reviews
from ..run import app
from uuid import uuid4


class Test_User_Routes(unittest.TestCase):

    def setupUserInstance1(self):
        userObj1 = User(12323231313, 'louis', 'louis@eemail.com', generate_password_hash('password'))                
    
    def setupUserInstance2(self):
        userObj2 = User(23434234234, 'james', 'james@email.com', generate_password_hash('password1'))

    def test_user_secrey_key(self):
        pass
        # global SECRETKEY
        # res = 'thisISverysecret'
        # self.assertEqual(res, SECRETKEY)
    
    def test_user_registration(self):
        # response = self.client.post('/api/v1/auth/register', content_type='application/json',
        #                             data=json.dumps({"userid":str(uuid4()), "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        # response_data = json.loads(response.data.decode())
        
        self.assertEqual(200, response_data['message'])
        
class Test_Business_Routes(unittest.TestCase):

    def setUp(self):
        # busObj = Business('12345', 'somebusiness', 'somelocation', 'somecategory', 'somedescription')
        # self.assertIsInstance(busObj, Business)
        pass

# class Test_Review_Routes(unittest.TestCase):

#     def setUp(self):
#         revObj = Reviews('12345', '12345', 'this is an example review')
#         self.assertIsInstance(revObj, Reviews)



if __name__ == '__main__':
    unittest.main()