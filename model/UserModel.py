from mongoengine import Document, StringField
from flask_auth.monogengine_auth.AuthModel import Auth
from flask_auth.monogengine_auth.AuthController import Authorization #isAllowed

class UserModel(Document, Auth):
    email = StringField()
    name = StringField()

authorization = Authorization(UserModel)