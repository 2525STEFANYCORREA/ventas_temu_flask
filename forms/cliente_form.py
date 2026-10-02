from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ClienteForm(FlaskForm):
    """Formulario para registrar o editar clientes."""

    nombre = StringField(
        "Nombre completo",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres."),
        ],
    )
    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Length(min=7, max=20, message="Ingresa un teléfono válido."),
        ],
    )
    correo = StringField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio."),
            Email(message="Ingresa un correo electrónico válido."),
        ],
    )
    estado = SelectField(
        "Estado",
        choices=[
            ("Activo", "Activo"),
            ("Pendiente", "Pendiente"),
        ],
        validators=[DataRequired(message="Selecciona un estado.")],
    )
    submit = SubmitField("Guardar cliente")
