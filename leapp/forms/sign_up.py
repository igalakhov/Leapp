from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import equal_to, input_required, length
from wtforms.fields.html5 import EmailField


class SignUpForm(FlaskForm):
    first_name = StringField('First Name:',
                             validators=[input_required('This field is required.'),
                                         length(3, 127)])
    last_name = StringField('Last Name:',
                            validators=[input_required('This field is required'),
                                        length(3, 127)])

    password = PasswordField('Password:',
                             validators=[input_required('This field is required.'),
                                         length(7, 127)])
    password_confirm = PasswordField('Repeat Password:',
                                     validators=[input_required('This field is required.'),
                                                 equal_to('password', 'Your passwords should probably be the same'),
                                                 length(7, 127)])

    email = EmailField('Email:')
    email_confirm = BooleanField('Sign me up for an occasional email about current and future plans',
                                 default=True)

    submit = SubmitField("Sign Up")

