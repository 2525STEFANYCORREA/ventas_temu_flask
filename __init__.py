"""Formularios Flask-WTF del sistema Ventas Temu.

Las clases se mantienen separadas por módulo para facilitar la futura
integración con persistencia y bases de datos.
"""
from .producto_form import ProductoForm
from .cliente_form import ClienteForm
from .proveedor_form import ProveedorForm
from .facturacion_form import FacturacionForm

__all__ = [
    "ProductoForm",
    "ClienteForm",
    "ProveedorForm",
    "FacturacionForm",
]

from .login_form import LoginForm
from .usuario_form import UsuarioForm
