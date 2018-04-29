[![Build Status](https://travis-ci.org/louiCoder/WeConnect-API.svg?branch=feature)](https://travis-ci.org/louiCoder/WeConnect-API) [![Maintainability](https://api.codeclimate.com/v1/badges/a6c406da1fffc6d5fb75/maintainability)](https://codeclimate.com/github/louiCoder/WeConnect-API/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/louiCoder/WeConnect-API/badge.svg?branch=feature)](https://coveralls.io/github/louiCoder/WeConnect-API?branch=feature)


<!-- [![Test Coverage](https://api.codeclimate.com/v1/badges/a6c406da1fffc6d5fb75/test_coverage)](https://codeclimate.com/github/louiCoder/WeConnect-API/test_coverage) -->

# WeConnect-API
WeConnect API using Python, Flask-RestFul 

WeConnect-Api provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.

#### Author:
    Louis Musanje Michael

#### project captures the following routes 

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST | /api/auth/register | creating user account |
| POST | api/auth/login | logging in for a user |
| POST | api/auth/logout | Logs out a user |
| POST | api/auth/reset-password | Password reset |
| POST | api/businesses | Registering a business |
| PUT | api/businesses/<_businessId_> | Updating a business profile |
| DELETE | api/businesses/<_businessId_> | delete/remove a business profile |
| GET | api/businesses | gets all avaliable businesses |
| GET | api/businesses/<_businessId_> | Get a business |
| POST | api/businesses/<_businessId_>/reviews | Add a review for a business |
| GET | api/businesses/<_businessId_>/reviews | Get all reviews for a business |



#### Technologies and Tools used to develop this App
1. Bootstrap Framework (Html5 + CSS3 + Javascript)
2. Jquery
3. Python
4. Postman
5. VSCODE (for editing and debugging)

#### Project dependencies Will always be found in the file below
    requirements.txt

#### Set up project to get it up and running
* clone repository from link below  
  
      $ git clone https://github.com/louiCoder/WeConnect-API.git

* Set up Virtual environment by running commands below

      * virtualenv venv
      * source /venv/Scripts/activate (for linux/mac)
      * /venv/Scripts/activate.exe (for windows)

#### The application is Hosted on Heroku on the link below.
    
http://we-connect-louis.herokuapp.com or http://we-connect-louis.herokuapp.com/apidocs/

#### Get all project dependencies by running the command below.

      $ pip freeze -r requirements.txt
      
#### To run the unit tests invoke/run the command below.

      $ nosetests tests or nosetests

#### or for detailed output on unit tests run with verbose.

      $ nosetests --with-coverage -v
      
#### To run the application invoke the command below.

      $ python app.py
      
 #### Now that the server is running , open your browser and run one of the links below.

      $ localhost:5000  or  127.0.0.1:5000

