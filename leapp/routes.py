from flask import Flask, render_template, flash, redirect
from leapp.forms.sign_up import SignUpForm
from leapp.models.models import User
from leapp.models import db
from leapp import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='LEΛPP')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    valid_data = True

    if form.validate_on_submit():
        # everything is fine, possibly make a new account
        flash('cool form dude', 'success')

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

    elif len(form.errors) > 0 or not valid_data:
        flash('Please correct the errors below.', 'danger')

    return render_template('sign_up.html',
                           title='Sign Up',
                           sign_up_form=form)