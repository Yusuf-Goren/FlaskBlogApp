
from urllib import response
from blog.services import blog_services
from flask import Blueprint, request
from helpers import token_required
BLOG = Blueprint('BLOG', __name__)


@BLOG.get("/")
@token_required
def get_all_blogs(current_user):
    response = blog_services.get_all_blogs()
    return response


@BLOG.get("/blog/<blog_id>")
@token_required
def get_one_blog(current_user, blog_id):
    response = blog_services.get_one_blog(request, blog_id)
    return response


@BLOG.get("/blog/user/<user_id>")
@token_required
def get_one_user_blogs(current_user, user_id):
    response = blog_services.get_one_user_blogs(request, user_id)
    return response


@BLOG.post("/write")
@token_required
def create_blog(current_user):
    response = blog_services.create_blog(current_user, request)
    return response


@BLOG.put("/blog/<blog_id>")
@token_required
def edit_blog(current_user, blog_id):
    response = blog_services.edit_blog(current_user, blog_id)
    return response


@BLOG.delete("/blog/<blog_id>")
@token_required
def delete_blog(current_user, blog_id):
    print(blog_id)
    response = blog_services.delete_blog(current_user, blog_id)
    return response


@BLOG.get("/blog-like/<blog_id>")
@token_required
def like(current_user, blog_id):
    response = blog_services.like(current_user, blog_id)
    return response


@BLOG.get("/blog-like/blogs/<blog_id>")
@token_required
def like_blogs(current_user, blog_id):
    response = blog_services.like_blogs(current_user, blog_id)
    return response


@BLOG.get("/blog-like/users/<user_id>")
@token_required
def like_users(current_user, user_id):
    response = blog_services.like_users(current_user, user_id)
    return response
