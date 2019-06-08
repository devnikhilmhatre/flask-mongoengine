from flask_restful import Resource
from model.PostModel import *
from model.UserModel import UserModel
from json import loads, dumps
from serializers.PostSerializer import PostSchema


class PostController(Resource):
    def get(self):

        data = PostModel.objects.aggregate(*[
            {
                '$lookup':{
                    'from': UserModel._get_collection_name(),
                    'localField':'author',
                    'foreignField':'_id',
                    'as':'User'
                }
            }
        ])

        # for i in data:
        #     print(i)
        schema = PostSchema(many=True)
        
        # s = schema.dump(data).data
        
        # print(list(data._CommandCursor__data))
        # return {}
        # return loads(dumps(data))

        '''Embedded document test'''
        # c1 = CommentsModel(content="123")
        # c2 = CommentsModel(content="213")
        # for i in PostModel.objects():
        #     i.comments = [c1, c2]
        #     i.save()
        
        return schema.dump(data).data

        '''Dynamic document, dict field, list field test '''
        # Page(t="1230", dd={'1':1,'2':2}).save()
        # for p in Page.objects:
            # p.abc = [{"anc":'jshjkasd', "jsdbasjkd":122312153}, {"anc":'jshjkasd', "jsdbasjkd":122312153}]
            #  =  datetime.datetime.now()
            # print(p.d)
            # p.save()
        # return loads(Page.objects.to_json())