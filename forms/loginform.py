from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, EmailField, StringField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField('Логин', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
