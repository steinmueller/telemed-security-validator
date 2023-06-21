#Routes for the Website
from flask import session, make_response, Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .utils import get_oidc, get_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        oidc = get_oidc()
        token = get_token(oidc, email, password)

        response = make_response(redirect(url_for('views.home')))

        if token:
            response.set_cookie('access_token', token['access_token'])
            session['access_token'] = token['access_token']
            session['username'] = email
        return response # TODO eins weiter einrücken?
    return render_template("login.html", user=current_user)
        
    #     #validate
    #     user = User.query.filter_by(email=email).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             flash('Login successful!', category='success')
    #             login_user(user, remember=True)
    #             return redirect(url_for('views.home'))
    #         else:
    #             flash('Incorrect Password!', category='error')
    #     else:
    #         flash('Wrong Email!', category='error')
    # return render_template("login.html", user=current_user)

@auth.route('/logout')
# @login_required
#@oidc.require_login
def logout():
    # logout_user()
    # return redirect(url_for('auth.login'))
    session.pop('username', None)
    session.pop('access_token', None)
    return redirect(url_for(views.login))

# @auth.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('Email already exists.', category='error')
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters.', category='error')
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 7:
#             flash('Password must be at least 7 characters.', category='error')
#         else:
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template("sign_up.html", user=current_user)   