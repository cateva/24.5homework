from ast import Pass
from turtle import title
from wsgiref.validate import validator
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
form flask_wtf import FlaskForm

class LoginForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1,max=20)]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired() Length(min=6, max=55)]
    )

class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1,max=20)]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired() Length(min=6, max=55)]
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
    )

class FeedbackForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Content",
        validators=[InputRequired(), Length(max=10000)],
    )

class DeleteForm(FlaskForm):
    

    