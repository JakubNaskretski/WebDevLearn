from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# have 2 import validators for fieldds
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    # Username also as a label in html
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('ConfirmPassword',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    # 'Email' also as a label in html
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class GreetingForm(FlaskForm):
        name = StringField('Name',
                            validators=[Length(min=0, max=20)])
        submit = SubmitField('Greet Me !')
