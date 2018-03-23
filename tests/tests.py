import unittest
from flask import Blueprint, Flask, request, json, jsonify, make_response, Response
# from views.business.businessModel import Business
# from views.user.userModel import User
# from ..views.user.views import 
from ..run import app
from uuid import uuid4


class Test_User_Routes(unittest.TestCase):

    def setUp(self):
        # userObj = User('23423423', 'louis', 'louis@eemail.com', 'This#is#secret')
        # self.assertIsInstance(userObj, User)
        self.client = app.test_client()
        # self.response = self.client.get('/', follow_redirects=True)
        

    def test_user_secrey_key(self):
        pass
        # global SECRETKEY
        # res = 'thisISverysecret'
        # self.assertEqual(res, SECRETKEY)
    
    def test_user_registration(self):
        response = self.client.post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"userid":str(uuid4()), "username": "fsfsf", "password": "somepassword", "email": "some@email.com"}))
        response_data = json.loads(response.data.decode())
        self.assertEqual('User has been Successfully registered.', response_data['message'])
        
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