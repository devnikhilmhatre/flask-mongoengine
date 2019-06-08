from flask import Flask
from flask_restful import Api
from mongoengine import connect

# Controllers
from controllers.PostController import PostController
from controllers.UserController import UserController
from controllers.LoginController import LoginController


# mongo connection
connect('flask_mongoengine')


# app
app = Flask(__name__)
api = Api(app)


# End Points
api.add_resource(UserController, '/users/')
api.add_resource(PostController, '/posts/')
api.add_resource(LoginController, '/login/')


if __name__ == '__main__':
    app.run(debug=True)