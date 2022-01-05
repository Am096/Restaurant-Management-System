
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField


class RegisterForm(FlaskForm):
    username = StringField('User Name:')
    password = PasswordField('Password :')
    submit = SubmitField('SUBMIT')


class menuForm(FlaskForm):
    dishname = StringField('DISH NAME:')
    dishprice = IntegerField('DISH PRICE :')
    submit = SubmitField('CONFIRM')
