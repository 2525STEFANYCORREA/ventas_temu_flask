from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProveedorForm(FlaskForm):
    """Formulario para registrar o editar proveedores."""

    nombre = StringField(
        "Nombre del proveedor",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres."),
        ],
    )
    contacto = StringField(
        "Información de contacto",
        validators=[
            DataRequired(message="El contacto es obligatorio."),
            Length(min=5, max=150, message="Debe tener entre 5 y 150 caracteres."),
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
    submit = SubmitField("Guardar proveedor")
