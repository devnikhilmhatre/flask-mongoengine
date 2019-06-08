from mongoengine import StringField, BooleanField, DateTimeField
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
import uuid
import jwt


class Auth:
    username = StringField(required=True)
    password = StringField(required=True)
    salt = StringField(required=True)
    token = StringField(default='')

    # roles
    admin = BooleanField(default=False)
    staff = BooleanField(default=False)
    public = BooleanField(default=False)

    is_active = BooleanField(default=False)


    def create_token(self):
        token = str(uuid.uuid4())
        self.token = token
        return jwt.encode({'token':token}, 'd7111bfe-6fcf-441c-ae81-529be2ba5015', algorithm='HS256').decode()
    
    @staticmethod
    def verify_token(token):
        try:
            return jwt.decode(token, 'd7111bfe-6fcf-441c-ae81-529be2ba5015', algorithms=['HS256'])['token']
        except Exception as e:
            return ''

    def set_password(self, password):
        _hash = pbkdf2_sha256.using(rounds=35719).hash(password).split('$')
        self.password = _hash[4]
        self.salt = _hash[3]
    
    def verify_password(self, password):
        _hash = '$pbkdf2-sha256$35719${}${}'.format(self.salt, self.password)
        return pbkdf2_sha256.verify(password, _hash)