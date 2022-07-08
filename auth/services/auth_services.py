
from flask import jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from model import User
from app import db, app


def submit(requst):
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = generate_password_hash(
        request.form['password'], method='sha256')

    user = User(fname, lname, email, password)
    db.session.add(user)
    db.session.commit()
    return {'message': '.New User created'}


def login(request):
    auth = request.form
    if not auth or not auth.get('email') or not auth.get('password'):

        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user = User.query.filter_by(email=auth.get('email')) .first()

    password = request.form['password']
    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30000)}, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})

    print("Invalid identity")
    return "Invalid identity "
