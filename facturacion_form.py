from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class FacturacionForm(FlaskForm):
    numero = StringField("Número de factura", validators=[
        DataRequired(message="El número de factura es obligatorio."),
        Length(min=3, max=20, message="Debe tener entre 3 y 20 caracteres.")
    ])
    cliente = SelectField("Cliente", choices=[], coerce=int,
        validators=[DataRequired(message="Selecciona un cliente.")])
    total = FloatField("Total", validators=[
        DataRequired(message="El total es obligatorio."),
        NumberRange(min=0.01, message="El total debe ser mayor que 0.")
    ])
    estado = SelectField("Estado", choices=[
        ("Pagada", "Pagada"), ("Pendiente", "Pendiente"), ("Anulada", "Anulada")
    ], validators=[DataRequired(message="Selecciona un estado.")])
    submit = SubmitField("Guardar factura")
