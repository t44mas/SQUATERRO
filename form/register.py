from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    preferences = StringField('preferences')
    allergies = StringField('allergies')
    blacklisted = StringField('blacklisted')
    submit = SubmitField('Submit')