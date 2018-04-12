import flask
from flask import Flask
# from views.user.views import userBlueprint
from views.user.views import userBlueprint
from views.business.views import businessBlueprint
from views.reviews.views import reviewBlueprint
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
app.register_blueprint(userBlueprint)
app.register_blueprint(businessBlueprint)
app.register_blueprint(reviewBlueprint)


#swagger docs instanciation
swagger = Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)