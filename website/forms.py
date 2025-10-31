from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')  


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Log In')