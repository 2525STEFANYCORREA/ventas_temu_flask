from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    usuario = StringField(
        "Usuario",
        validators=[
            DataRequired(message="Ingresa tu usuario."),
            Length(min=3, max=50),
        ],
    )
    password = PasswordField(
        "Contraseña",
        validators=[DataRequired(message="Ingresa tu contraseña.")],
    )
    submit = SubmitField("Iniciar sesión")
