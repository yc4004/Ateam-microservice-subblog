from flask_restful import Resource, reqparse
from models.comment import CommentModel
from datetime import datetime
from google.oauth2 import id_token
from google.auth.transport import requests


CLIENT_ID = "917121905012-jt7do84gpaurpefgsljbme3dqes29gim.apps.googleusercontent.com"

class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('content',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('token',
        type=str,
        required=True,
        help='Every item needs a token.'
    )

    def get(self, token, blog_id):
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            user_id = idinfo['email'][0: idinfo['email'].index('@')]

            comment = CommentModel.find_by_blog_id(blog_id)
            if comment:
                return comment.json()
            return {'message': 'comment not found'}, 404

        except ValueError:
            print("Auth went wrong!")
            pass
    

    def post(self, user_id, blog_id):
        # if CommentModel.find_by_name(name):
        #     return {'message': "An comment with name '{}' already exists.".format(name)}, 400
        try:
            data = Comment.parser.parse_args()
            # print(data)
            # print('\n')
            token = data['token']
            # print(token)
            
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
            auth_user_id = idinfo['email'][0: idinfo['email'].index('@')]

            comment_time = str(datetime.now().date())

            if auth_user_id == user_id:
                comment = CommentModel(data['content'], blog_id, user_id, comment_time)
            try:
                comment.save_to_db()
            except:
                return {'message': 'An error occurred inserting the item.'}, 500  # Internal server error

            return comment.json(), 201

        except ValueError:
            print("Auth went wrong!")
            pass


    # def put(self, name):       
    #     data = Comment.parser.parse_args()
    #     comment = CommentModel.find_by_name(name)
    #     # updated_item = ItemModel(name, data['price'])

    #     if not comment:
    #         comment = CommentModel(name, data['Blog_id'])
    #     else:
    #         comment.content = data['content']
        
    #     comment.save_to_db()
        
    #     return comment.json()


class CommentList(Resource):
    def get(self):
        comments = [comment.json() for comment in CommentModel.find_all()]
        return {'comment': comments}, 200
        


class Delete(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id',                          
        type=int,
        required=True,
        help='This field cannot be left blank'
    )

    def delete(self, user_id, blog_id):

        data = Delete.parser.parse_args()
        id = data['id']

        comment = CommentModel.find_by_id(id)
        if comment:
            comment.delete_from_db()
            return {'message': 'Comment deleted'}
     

        