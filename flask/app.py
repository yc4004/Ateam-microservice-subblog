
from flask import Flask, jsonify, Response
from flask_restful import Api
from db import db
import json

from resources.blog import Blog, BlogList
from resources.comment import Comment, CommentList
from flask_cors import CORS
from comment_resource import CommentResource

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:84443295412lx.@localhost/commentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'yanbing'  # app.config['JWT_SECRET_KEY']
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Blog, '/blog/<string:title>')
api.add_resource(BlogList, '/blogs')
api.add_resource(Comment, '/posts/<string:blog_id>/addcomment')
api.add_resource(CommentList, '/comments')


@app.route("/posts/<blog_id>", methods=["GET"])
def get_comments_by_blogid(blog_id):
    result = CommentResource.get_comments_by_blogID(blog_id)
    if result:
        response = Response(json.dumps(result, default=str), status=200, content_type="application/json")
    else:
        response = Response("404 NOT FOUND", status=404, content_type="application/json")
    return response


# make it only run when we run python app.py, not for other files import app.py
# only the file you run is '__main__'
if __name__ == '__main__':
    db.init_app(app)
    # app.run(port=5011, debug=True)
    app.run(host="0.0.0.0", port=5011)
    
