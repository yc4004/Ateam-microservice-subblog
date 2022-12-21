from flask import Flask, jsonify, Response, request, render_template, redirect, url_for, session
from flask_restful import Api
from db import db
import json
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_cors import CORS

from resources.comment import CommentList, Delete as deleteComment, Comment as addComment
from flask_cors import CORS
from comment_resource import CommentResource


app = Flask(__name__)

CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:84443295412lx.@localhost/commentdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:dbuserdbuser@user-db.chowgm8mh4hg.us-east-1.rds.amazonaws.com/commentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'yanbing'  # app.config['JWT_SECRET_KEY']
api = Api(app)

CLIENT_ID = "917121905012-jt7do84gpaurpefgsljbme3dqes29gim.apps.googleusercontent.com"

@app.before_first_request
def create_tables():
    db.create_all()     


api.add_resource(addComment, '/<string:user_id>/posts/<string:blog_id>/addcomment')
api.add_resource(deleteComment, '/<string:user_id>/posts/<string:blog_id>/deletecomment')
api.add_resource(CommentList, '/comments')


@app.route("/posts/<blog_id>/getcomments", methods=["GET"])
def get_comments_by_blogid(blog_id):
    result = CommentResource.get_comments_by_blogID(blog_id)
    if result:
        response = Response(json.dumps(result, default=str), status=200, content_type="application/json")
    else:
        response = Response("404 NOT FOUND", status=404, content_type="application/json")

    return response


@app.route("/posts/<blog_id>/getcommentsnum", methods=["GET"])
def get_commentsnum_by_blogid(blog_id):
    comment_num = str(CommentResource.get_comments_number(blog_id))
    return Response(comment_num, status=200, content_type="application/json")


@app.route("/commentnumber", methods=["GET"])
def get_comment_number_by_username():
    username = request.args.get('username')
    comment_num = str(CommentResource.get_commentsnum_by_username(username))
    response = Response(comment_num, status=200, content_type="application/json")
    return response


@app.route("/posts/checkbeforeDelete", methods=["POST"])
def jwtAuthBeforeDelete():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jwt_body = request.json
        jwt_token = jwt_body['token']  # getting the jwt token
        try:
            idinfo = id_token.verify_oauth2_token(jwt_token, requests.Request(), CLIENT_ID)
            owner_id = idinfo['email'][0: idinfo['email'].index('@')]
            message = {"owner_id": owner_id}
            return Response(json.dumps(message, default=str), status=200, content_type="application/json")

        except ValueError:
            print("Auth went wrong!")
            pass


# make it only run when we run python app.py, not for other files import app.py
# only the file you run is '__main__'
if __name__ == '__main__':
    db.init_app(app)
    app.run(host="0.0.0.0", port=5013)