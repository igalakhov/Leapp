from flask import Flask, render_template, flash, redirect, Blueprint
from app.forms.sign_up import SignUpForm
from app.forms.log_in import LogInForm
from app.models.models import User
from app.models import db


public_views = Blueprint('thing', __name__)


@public_views.route('/')
@public_views.route('/index')
def index():
    return render_template('index.html',
                           title='LEΛPP')


@public_views.route('/signup', methods=['GET', 'POST'])
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
def log_in():
    form = LogInForm()

    if form.validate_on_submit():
        flash('Cool form dude', 'success')

    return render_template('log_in.html',
                           title='Log In',
                           log_in_form=form)
