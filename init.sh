export FLASK_APP=main.py
export FLASK_ENV=thesis
export KEYCLOAK_FLASK_SETTINGS=settings.py
source environments/thesis/bin/activate
flask run
