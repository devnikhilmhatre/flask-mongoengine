from flask_restful import Resource, request
from model.UserModel import UserModel, authorization
from json import loads
from serializers.UserSerializer import UserSerializer

class LoginController(Resource):
    def post(self):
        response = authorization.login(request.json['username'], request.json['password'])
        if not response['error']:
            serializer = UserSerializer()
            user = serializer.dump(response['user'])
            return {"user":user.data, "token":response['token']}
        return {} 
    