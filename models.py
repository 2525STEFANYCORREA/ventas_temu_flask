from flask_login import UserMixin


class Usuario(UserMixin):
    """Representa un usuario autenticado de la tabla usuarios."""

    def __init__(self, id, usuario, password):
        self.id = int(id)
        self.usuario = usuario
        self.password = password

    def get_id(self):
        return str(self.id)
