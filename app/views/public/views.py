from flask import Flask, render_template, flash, redirect, Blueprint, url_for
from functools import wraps
from app.forms.sign_up import SignUpForm
from app.forms.log_in import LogInForm
from app.models.models import User
from app.models import db

from flask_login import login_user, current_user, logout_user


# login not required decorator
def anonymous_required(f):

    @wraps(f)
    def actual_decorator(*args, **kwargs):
        if current_user.is_anonymous:
            return f(*args, **kwargs)

        flash('Please log out to view this page')
        return redirect(url_for('public.index'))

    return actual_decorator


public_views = Blueprint('public', __name__)


@public_views.route('/')
@public_views.route('/index')
def index():
    return render_template('index.html',
                           title='LEΛPP')


@public_views.route('/signup', methods=['GET', 'POST'])
@anonymous_required
def signup():
    form = SignUpForm()

    valid_data = True

    if form.validate_on_submit():
        # everything is fine, possibly make a new account

        if len(User.query.filter_by(email=form.email.data).all()) > 0:
            flash('An account with this email already exists.', 'danger')
            valid_data = False

        # more checks as necessary

        if valid_data:
            new_user = User(form.first_name.data,
                            form.last_name.data,
                            form.email.data,
                            form.password.data,
                            form.password_confirm.data)

            db.session.add(new_user)
            db.session.commit()

            flash('New account created! Log in below.', 'success')
            return redirect('/login')

    elif len(form.errors) > 0 or not valid_data:
        flash('Please correct the errors below.', 'danger')

    return render_template('sign_up.html',
                           title='Sign Up',
                           sign_up_form=form)


@public_views.route('/login', methods=["GET", "POST"])
@anonymous_required
def login():
    form = LogInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.validate_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('public.login'))

        flash('You should be logged in now', 'success')
        login_user(user)

    return render_template('log_in.html',
                           title='Log In',
                           log_in_form=form)


@public_views.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out!')
    return redirect(url_for('public.login'))


@public_views.route('/logindata')
def data_stuff():
    if current_user.is_anonymous:
        return str('NO LOGIN HERE')
    return str('LOGGED IN AS ' + current_user.email)

