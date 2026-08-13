from flask import Flask, render_template

app = Flask(__name__)

productos = [
    {"nombre": "Audífonos Bluetooth", "categoria": "Tecnología", "precio": 8.99, "emoji": "🎧"},
    {"nombre": "Bolso casual", "categoria": "Moda", "precio": 12.50, "emoji": "👜"},
    {"nombre": "Organizador para hogar", "categoria": "Hogar", "precio": 6.75, "emoji": "🏠"},
    {"nombre": "Set de maquillaje", "categoria": "Belleza", "precio": 9.80, "emoji": "💄"},
]

clientes = [
    {"nombre": "María López", "telefono": "099 111 2233", "correo": "maria@email.com"},
    {"nombre": "Carlos Zambrano", "telefono": "098 222 3344", "correo": "carlos@email.com"},
]

proveedores = [
    {"nombre": "Temu Marketplace", "contacto": "Atención en línea", "estado": "Activo"},
    {"nombre": "Proveedor Internacional 02", "contacto": "Pedidos bajo solicitud", "estado": "Activo"},
]

facturas = [
    {"numero": "F-001", "cliente": "María López", "total": 24.49, "estado": "Pagada"},
    {"numero": "F-002", "cliente": "Carlos Zambrano", "total": 18.75, "estado": "Pendiente"},
]


@app.route("/")
def inicio():
    return render_template("index.html", productos=productos)


@app.route("/productos")
def productos_view():
    return render_template("productos.html", productos=productos)


@app.route("/clientes")
def clientes_view():
    return render_template("clientes.html", clientes=clientes)


@app.route("/proveedores")
def proveedores_view():
    return render_template("proveedores.html", proveedores=proveedores)


@app.route("/facturacion")
def facturacion_view():
    return render_template("facturacion.html", facturas=facturas)


if __name__ == "__main__":
    app.run(debug=True)
