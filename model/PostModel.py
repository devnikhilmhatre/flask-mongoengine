from mongoengine import *
from .UserModel import UserModel
from datetime import datetime

class Page(DynamicDocument):
    t = StringField()
    dd = DictField()
    u = UUIDField()

class CommentsModel(EmbeddedDocument):
    content = StringField()


class PostModel(Document):
    title = StringField()
    author = ReferenceField(UserModel, reverse_delete_rule=CASCADE)
    tags = ListField(StringField())
    comments = ListField(EmbeddedDocumentField(CommentsModel))

    meta = {'allow_inheritance': True}


class TextPostModel(PostModel):
    content = StringField()


class ImagePostModel(PostModel):
    image_path = StringField()
