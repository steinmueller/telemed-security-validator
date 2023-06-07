from flask import Flask, url_for

def create_app():
    #sp = TnaServiceProvider()

    app = Flask(__name__)

    # TODO Never share - Is there any more security measure necessary???
    app.config['SECRET_KEY'] = 'abnolreizug890a349ghil23r847t90p8grhfaio'

    # import blueprints
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    

    return app