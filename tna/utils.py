from keycloak import KeycloakAdmin, KeycloakOpenID
from flask import current_app

def get_oidc():
    return KeycloakOpenID(server_url=current_app.config.get('SERVER_URL'),
                          client_id=current_app.config.get('CLIENT_ID'),
                          realm_name=current_app.config.get('REALM_NAME'),
                          client_secret_key=current_app.config.get('CLIENT_SECRET'),
                          verify=True)

def get_token(oidc, username, pw):
    try:
        return oidc.token(username, pw)
    except Exception as e:
        print("Exception occurrs!\n%s" % e)
    return None