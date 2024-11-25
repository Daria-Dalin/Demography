from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, EmailField, StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email

class NewsForm(FlaskForm):
    title= StringField('Заголовок', validators=[DataRequired()])
    content=TextAreaField('Содержание')
    is_private = BooleanField("Личное")
    submit=SubmitField('Применить')