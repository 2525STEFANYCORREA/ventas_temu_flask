from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
# DATOS DE EJEMPLO - SEMANA 10
# ============================================================

nombre_sistema = "Ventas Temu"
empresa = {
    "nombre": "Ventas Temu",
    "descripcion": "Sistema web para gestionar productos, clientes, proveedores y facturación.",
    "version": "3.0 - Semana 10"
}

productos = [
    {"id": 1, "nombre": "Vestido casual", "categoria": "Ropa", "precio": 12.99, "stock": 15, "imagen": "producto-1.svg"},
    {"id": 2, "nombre": "Zapatillas deportivas", "categoria": "Calzado", "precio": 24.50, "stock": 8, "imagen": "producto-2.svg"},
    {"id": 3, "nombre": "Bolso de mano", "categoria": "Accesorios", "precio": 18.75, "stock": 0, "imagen": "producto-3.svg"},
    {"id": 4, "nombre": "Reloj digital", "categoria": "Accesorios", "precio": 9.99, "stock": 21, "imagen": "producto-4.svg"},
    {"id": 5, "nombre": "Camiseta básica", "categoria": "Ropa", "precio": 7.50, "stock": 30, "imagen": "producto-5.svg"},
    {"id": 6, "nombre": "Mochila escolar", "categoria": "Bolsos", "precio": 16.80, "stock": 5, "imagen": "producto-6.svg"},
]

clientes = [
    {"id": 1, "nombre": "María López", "telefono": "099 111 2233", "correo": "maria@example.com", "estado": "Activo"},
    {"id": 2, "nombre": "Carlos Pérez", "telefono": "098 222 3344", "correo": "carlos@example.com", "estado": "Activo"},
    {"id": 3, "nombre": "Ana Torres", "telefono": "097 333 4455", "correo": "ana@example.com", "estado": "Pendiente"},
    {"id": 4, "nombre": "José Zambrano", "telefono": "096 444 5566", "correo": "jose@example.com", "estado": "Activo"},
]

proveedores = [
    {"id": 1, "empresa": "Temu Marketplace", "contacto": "Equipo comercial", "telefono": "01 800 000 000", "estado": "Activo"},
    {"id": 2, "empresa": "Global Fashion", "contacto": "Laura Chen", "telefono": "02 555 1020", "estado": "Activo"},
    {"id": 3, "empresa": "Accesorios Express", "contacto": "Miguel Wang", "telefono": "03 555 2080", "estado": "Pendiente"},
]

facturas = [
    {"numero": "FAC-001", "cliente": "María López", "fecha": "18/08/2026", "total": 49.98, "estado": "Pagada"},
    {"numero": "FAC-002", "cliente": "Carlos Pérez", "fecha": "18/08/2026", "total": 24.50, "estado": "Pendiente"},
    {"numero": "FAC-003", "cliente": "Ana Torres", "fecha": "19/08/2026", "total": 18.75, "estado": "Pendiente"},
    {"numero": "FAC-004", "cliente": "José Zambrano", "fecha": "19/08/2026", "total": 31.79, "estado": "Pagada"},
]


@app.route("/")
def index():
    resumen = {
        "productos": len(productos),
        "clientes": len(clientes),
        "proveedores": len(proveedores),
        "facturas": len(facturas),
        "ventas": sum(f["total"] for f in facturas),
    }
    return render_template(
        "index.html",
        nombre_sistema=nombre_sistema,
        empresa=empresa,
        resumen=resumen,
        productos=productos[:4],
        facturas=facturas[:4],
    )


@app.route("/productos")
def productos_view():
    categorias = sorted({p["categoria"] for p in productos})
    return render_template(
        "productos.html",
        nombre_sistema=nombre_sistema,
        productos=productos,
        categorias=categorias,
    )


@app.route("/clientes")
def clientes_view():
    return render_template(
        "clientes.html",
        nombre_sistema=nombre_sistema,
        clientes=clientes,
    )


@app.route("/proveedores")
def proveedores_view():
    return render_template(
        "proveedores.html",
        nombre_sistema=nombre_sistema,
        proveedores=proveedores,
    )


@app.route("/facturacion")
def facturacion_view():
    total_facturado = sum(f["total"] for f in facturas)
    return render_template(
        "facturacion.html",
        nombre_sistema=nombre_sistema,
        facturas=facturas,
        total_facturado=total_facturado,
    )


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html", nombre_sistema=nombre_sistema), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
