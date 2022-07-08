from flask import jsonify, request
from model import Blog, Like
from app import db


def get_all_blogs():
    items = []
    for item in db.session.query(Blog).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def get_one_blog(current_user, blog_id):
    if(request.method == "GET"):
        items = []
        for item in Blog.query.filter_by(id=blog_id).all():
            del item.__dict__['_sa_instance_state']
            items.append(item.__dict__)
        return jsonify(items)


def get_one_user_blogs(current_user, user_id):
    items = []
    for item in Blog.query.filter_by(user_id=user_id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_blog(current_user, request):
    text = request.form['text']
    blog = Blog(text, user_id=current_user.id)
    db.session.add(blog)
    db.session.commit()
    return {'message': 'Blog created!'}


def edit_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if(current_user.id == blog.user_id or current_user.is_admin == True):
        text_updated = request.form['text']
        db.session.query(Blog).filter_by(id=blog_id).update(
            dict(text=text_updated)
        )
        blog = Blog.query.filter_by(id=blog_id)
        db.session.commit()
    else:
        return "Your not authorized!!"
    return 'blog'


def delete_blog(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id).first()
    if(current_user.id == blog.user_id or current_user.is_admin == True):
        db.session.query(Blog).filter(Blog.id == blog_id).delete()
        db.session.commit()
        return "Succesfully deleted!"
    else:
        return "Your not authorized!!"


def like(current_user, blog_id):
    blog = Blog.query.filter_by(id=blog_id)
    like = Like.query.filter_by(
        user_id=current_user.id, blog_id=blog_id).first()
    if not blog:
        return "Blog doesnt exist"
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(user_id=current_user.id, blog_id=blog_id)
        db.session.add(like)
        db.session.commit()
    return "Likes"


def like_blogs(current_user, blog_id):
    items = []
    for item in Like.query.filter_by(blog_id=blog_id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def like_users(current_user, user_id):
    items = []
    for item in Like.query.filter_by(user_id=user_id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)
