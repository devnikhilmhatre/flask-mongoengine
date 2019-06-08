from flask_restful import Resource, request
from model.UserModel import UserModel, authorization
from model.PostModel import TextPostModel
from flask_auth.monogengine_auth.generic import Generic
from json import loads

class UserController(Generic):
    model = UserModel
    # @authorization.isAllowed
    # def get(self, *args, **kwargs):
    #     # nikhil = UserModel.objects.get(name='nikhil')
    #     # post1 = TextPostModel(title='Fun with MongoEngine', author=nikhil)
    #     # post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    #     # post1.tags = ['mongodb', 'mongoengine']
    #     # post1.save()
    #     return loads(UserModel.objects().exclude('password', 'salt').to_json())
    
    # def post(self):
    #     password = request.json.pop('password')
    #     user = UserModel(**request.json)
    #     user.set_password(password)
    #     user.save()
    #     user = loads(user.to_json())
    #     user['_id'] = user['_id']['$oid']
    #     return user