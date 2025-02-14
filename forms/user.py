from wtforms.fields.simple import PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Отправить')
