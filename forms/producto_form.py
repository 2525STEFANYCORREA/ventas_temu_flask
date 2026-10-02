from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductoForm(FlaskForm):
    nombre = StringField("Nombre del producto", validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres.")
    ])
    categoria = SelectField("Categoría", choices=[
        ("Tecnología", "Tecnología"), ("Moda", "Moda"), ("Hogar", "Hogar"),
        ("Belleza", "Belleza"), ("Calzado", "Calzado"), ("Accesorios", "Accesorios"),
        ("Otros", "Otros")
    ], validators=[DataRequired(message="Selecciona una categoría.")])
    precio = FloatField("Precio", validators=[
        DataRequired(message="El precio es obligatorio."),
        NumberRange(min=0.01, message="El precio debe ser mayor que 0.")
    ])
    stock = IntegerField("Stock", validators=[
        DataRequired(message="El stock es obligatorio."),
        NumberRange(min=0, message="El stock no puede ser negativo.")
    ])
    emoji = StringField("Ícono", validators=[
        DataRequired(message="El ícono es obligatorio."),
        Length(min=1, max=10, message="Ingresa un ícono válido.")
    ])
    proveedor = SelectField("Proveedor", choices=[], coerce=int,
        validators=[DataRequired(message="Selecciona un proveedor.")])
    submit = SubmitField("Guardar producto")


class DeleteForm(FlaskForm):
    submit = SubmitField("Eliminar")
