from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/blog'
app.config['SECRET_KEY'] = 'secretKey'


db = SQLAlchemy()


with app.app_context():
    from auth.controllers.auth_controller import AUTH
    from blog.controllers.blog_controller import BLOG

    db.init_app(app)
    db.create_all()
    db.session.commit()
    migrate = Migrate(app, db)

    app.register_blueprint(AUTH, url_prefix='/')
    app.register_blueprint(BLOG, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)
