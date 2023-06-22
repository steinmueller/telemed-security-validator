from flask import Flask, url_for, g, session
#from keycloak import KeycloakOpenID
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config.from_envvar('KEYCLOAK_FLASK_SETTINGS')

    # # TODO Never share - Is there any more security measure necessary???
    app.config['SECRET_KEY'] = 'abnolreizug890a349ghil23r847t90p8grhfaio'
    # # TODO adapt to azure DB
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .models import User, Mission

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

app = create_app()

def get_app():
    return app

def create_database(app):
    if not path.exists('tna/' + DB_NAME):
        db.create_all(app = app)
        print('Database created')
