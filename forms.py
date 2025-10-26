from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired(), Length(min=8, max=12)])
    confirm_password = PasswordField('Confirm password', validators = [InputRequired(), Length(min=8, max=12), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Loginform(FlaskForm):
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired(), Length(min=8, max=12)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')