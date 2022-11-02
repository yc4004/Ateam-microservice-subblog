from db import db

class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50))
    content = db.Column(db.String(80))

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    blog = db.relationship('BlogModel')

    def __init__(self, content, blog_id):
        # self.name = name
        self.content = content
        self.blog_id = blog_id
    
    def json(self):
        return {
            'id': self.id, 
            # 'name': self.name,
            'content': self.content, 
            'blog_id': self.blog_id
        }
    
    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name=name).first()  # SELECT * FROM comments WHERE id=_id LIMIT 1

    @classmethod
    def find_all(cls):
        return cls.query.all()

    # update or insert
    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

