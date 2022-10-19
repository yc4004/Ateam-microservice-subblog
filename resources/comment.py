from flask_restful import Resource, reqparse
from models.comment import CommentModel


class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('content',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )
    parser.add_argument('blog_id',
        type=int,
        required=True,
        help='Every item needs a blog id.'
    )

    def get(self, name):
        comment = CommentModel.find_by_name(name)
        if comment:
            return comment.json()
        return {'message': 'comment not found'}, 404
    
    def post(self, name):
        if CommentModel.find_by_name(name):
            return {'message': "An comment with name '{}' already exists.".format(name)}, 400

        data = Comment.parser.parse_args()

        comment = CommentModel(name, data['content'], data['blog_id'])

        try:
            comment.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500  # Internal server error

        return comment.json(), 201 

    def delete(self, name):
        comment = CommentModel.find_by_name(name)
        if comment:
            comment.delete_from_db()

        return {'message': 'Comment deleted'}

    def put(self, name):       
        data = Comment.parser.parse_args()
        comment = CommentModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if not comment:
            comment = CommentModel(name, data['Blog_id'])
        else:
            comment.content = data['content']
        
        comment.save_to_db()
        
        return comment.json()


class CommentList(Resource):
    def get(self):
        comments = [comment.json() for comment in CommentModel.find_all()]
        return {'comment': comments}, 200
        