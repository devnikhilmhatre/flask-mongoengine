from marshmallow import Schema, fields
# from common import objectIdToString

class UserSerializer(Schema):
    _id = fields.Function(lambda obj: str(obj['_id']) if isinstance(obj,dict) else str(obj._id))
    class Meta:
        fields = (
            'email', 'name', 
            'admin', '_id',
            'staff', 'public', 
            'username'
            )