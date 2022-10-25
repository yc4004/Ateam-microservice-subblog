
from flask import Flask, jsonify
from flask_restful import Api
from db import db

from resources.blog import Blog, BlogList
from resources.comment import Comment, CommentList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:dbuserdbuser@subblogdb.c4qfxod7s5ol.us-east-1.rds.amazonaws.com/commentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'yanbing'  # app.config['JWT_SECRET_KEY']
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Blog, '/blog/<string:title>')
api.add_resource(BlogList, '/blogs')
api.add_resource(Comment, '/comment/<string:name>')
api.add_resource(CommentList, '/comments')


# make it only run when we run python app.py, not for other files import app.py
# only the file you run is '__main__'
if __name__ == '__main__':
    db.init_app(app)
    # app.run(port=5000, debug=True)
    app.run(host="0.0.0.0", port=5011)
    
