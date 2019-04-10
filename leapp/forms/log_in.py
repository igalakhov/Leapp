from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import input_required, length
from wtforms.fields.html5 import EmailField


# log in form
class LogInForm(FlaskForm):
    email = EmailField('Email:', validators=[input_required('This field is required.'),
                                             length(7, 127)])

    password = PasswordField('Password:',
                             validators=[input_required('This field is required.'),
                                         length(7, 127)])

    submit = SubmitField('Log In')
