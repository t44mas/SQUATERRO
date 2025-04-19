from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField
from wtforms.fields.choices import SelectMultipleField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets.core import CheckboxInput, ListWidget


class RegisterForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired()])
    preferences = SelectMultipleField('preferences', choices=[('vegan', 'Веган'), ('vegetarian', 'Вегетарианец')]
                                      , option_widget=CheckboxInput(), widget=ListWidget(prefix_label=False))
    allergies = SelectMultipleField('allergies', choices=[('nuts', 'Арахис'), ('Lactose', 'Лактоза')],
                                    option_widget=CheckboxInput(), widget=ListWidget(prefix_label=False))
    submit = SubmitField('Submit')
