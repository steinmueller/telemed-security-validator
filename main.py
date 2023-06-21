#import from __init__
from tna import get_app, views, auth

app = get_app()

from tna.views import views
from tna.auth import auth # TODO DAS HIER IST DAS PROBLEM!!!

# register blueprints
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)