
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    email = db.Column(db.String(40))
    likes = db.relationship(
        'Like', backref=db.backref('users', lazy=True))
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(200))

    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password


class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship(
        'Like', backref=db.backref('blogs', lazy=True))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id


class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete="CASCADE"))
    blog_id = db.Column(db.Integer, db.ForeignKey(
        'blogs.id', ondelete="CASCADE"))
