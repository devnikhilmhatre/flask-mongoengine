from flask_restful import Resource
from json import loads

class Generic(Resource):

    def __init_subclass__(cls):
        pass
    
    def get(self, *args, **kwargs):
        # print()
        # nikhil = UserModel.objects.get(name='nikhil')
        # post1 = TextPostModel(title='Fun with MongoEngine', author=nikhil)
        # post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
        # post1.tags = ['mongodb', 'mongoengine']
        # post1.save()
        return loads(self.model.objects().exclude('password', 'salt').to_json())
    
    def post(self):
        password = request.json.pop('password')
        user = UserModel(**request.json)
        user.set_password(password)
        user.save()
        user = loads(user.to_json())
        user['_id'] = user['_id']['$oid']
        return user