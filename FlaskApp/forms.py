from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField
from wtforms import validators

class CommentForm(FlaskForm):
    username = StringField('Nombre Completo',
                         [
        validators.DataRequired(message="campo nombre completo"),
        validators.Length(min=5, message="debe contener minimo 5 caracteres")
                         ])
    edad = IntegerField('Edad')
    email = EmailField('Email',
                       [
        validators.DataRequired("este campo es necesario"),
        validators.Email("debe ser un email valido")
                       ])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    username = StringField('Nombre Completo',
                        [
        validators.DataRequired(message="campo nombre completo"),
        validators.Length(min=5, message="debe contener minimo 5 caracteres")
                        ])
    password = PasswordField('PassWord')
    



