from marshmallow import Schema, fields
from serializers.UserSerializer import UserSerializer

class PostSchema(Schema):
    _id = fields.Function(lambda obj: str(obj['_id']))
    User = fields.Nested(UserSerializer, many=True)
    class Meta:
        fields = ('title', 'tags', 'comments', '_id','User')