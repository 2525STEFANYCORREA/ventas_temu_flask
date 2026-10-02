import os
from decimal import Decimal
from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from psycopg2 import Error

from forms import ClienteForm, FacturacionForm, LoginForm, ProductoForm, ProveedorForm, UsuarioForm
from forms.producto_form import DeleteForm
from conexion.conexion import ejecutar_sql, probar_conexion
from models import Usuario

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cambiar-en-produccion-ventas-temu-2026")
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Debes iniciar sesión para acceder a esta página."
login_manager.login_message_category = "warning"

nombre_negocio = "Ventas Temu"
mensaje_bienvenida = "Compra fácil, segura y al precio de la página + $4.75 por libra."


def inicializar_bd():
    """Crea las tablas si PostgreSQL está disponible."""
    statements = [
        """CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY, usuario VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS proveedores (
            id_proveedor SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL,
            contacto VARCHAR(150) NOT NULL, estado VARCHAR(20) NOT NULL DEFAULT 'Activo')""",
        """CREATE TABLE IF NOT EXISTS clientes (
            id_cliente SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL,
            cedula VARCHAR(20), telefono VARCHAR(20), correo VARCHAR(120),
            estado VARCHAR(20) NOT NULL DEFAULT 'Activo')""",
        """CREATE TABLE IF NOT EXISTS productos (
            id_producto SERIAL PRIMARY KEY, nombre VARCHAR(100) NOT NULL,
            categoria VARCHAR(60) NOT NULL, precio NUMERIC(10,2) NOT NULL CHECK (precio > 0),
            stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0), emoji VARCHAR(10) NOT NULL,
            id_proveedor INTEGER NOT NULL REFERENCES proveedores(id_proveedor)
            ON UPDATE CASCADE ON DELETE RESTRICT)""",
        """CREATE TABLE IF NOT EXISTS facturas (
            id_factura SERIAL PRIMARY KEY, numero VARCHAR(20) UNIQUE NOT NULL,
            id_cliente INTEGER REFERENCES clientes(id_cliente)
            ON UPDATE CASCADE ON DELETE SET NULL,
            fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            total NUMERIC(10,2) NOT NULL CHECK (total > 0),
            estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente')"""
    ]
    conn = None
    try:
        from conexion.conexion import obtener_conexion
        conn = obtener_conexion()
        with conn.cursor() as cur:
            for statement in statements:
                cur.execute(statement)
            cur.execute("""INSERT INTO proveedores (nombre, contacto, estado)
                SELECT 'Temu Marketplace','Atención en línea','Activo'
                WHERE NOT EXISTS (SELECT 1 FROM proveedores WHERE nombre='Temu Marketplace')""")
            cur.execute("""INSERT INTO proveedores (nombre, contacto, estado)
                SELECT 'Distribuciones Ecuador','Pedidos y logística','Activo'
                WHERE NOT EXISTS (SELECT 1 FROM proveedores WHERE nombre='Distribuciones Ecuador')""")
            cur.execute("""INSERT INTO clientes (nombre, cedula, telefono, correo, estado)
                SELECT 'María López','0900000001','099 111 2233','maria@email.com','Activo'
                WHERE NOT EXISTS (SELECT 1 FROM clientes WHERE correo='maria@email.com')""")
            cur.execute("""INSERT INTO clientes (nombre, cedula, telefono, correo, estado)
                SELECT 'Carlos Zambrano','0900000002','098 222 3344','carlos@email.com','Activo'
                WHERE NOT EXISTS (SELECT 1 FROM clientes WHERE correo='carlos@email.com')""")
        conn.commit()
    except Exception:
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


try:
    inicializar_bd()
except Exception:
    pass


@login_manager.user_loader
def load_user(user_id):
    try:
        rows = ejecutar_sql("SELECT id, usuario, password FROM usuarios WHERE id=%s", (user_id,), True)
        if rows:
            u = rows[0]
            return Usuario(u["id"], u["usuario"], u["password"])
    except Exception:
        pass
    return None


def usuario_por_nombre(nombre):
    rows = ejecutar_sql("SELECT id, usuario, password FROM usuarios WHERE usuario=%s", (nombre,), True)
    return rows[0] if rows else None


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = UsuarioForm()
    if form.validate_on_submit():
        try:
            usuario = form.usuario.data.strip()
            if usuario_por_nombre(usuario):
                flash("El nombre de usuario ya está registrado.", "warning")
            else:
                ejecutar_sql("INSERT INTO usuarios (usuario,password) VALUES (%s,%s)",
                             (usuario, generate_password_hash(form.password.data)))
                flash("Usuario registrado correctamente.", "success")
                return redirect(url_for("login"))
        except Exception:
            flash("No se pudo registrar el usuario.", "danger")
    return render_template("registro.html", form=form, nombre_negocio=nombre_negocio)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        try:
            u = usuario_por_nombre(form.usuario.data.strip())
            if u and check_password_hash(u["password"], form.password.data):
                login_user(Usuario(u["id"], u["usuario"], u["password"]))
                flash("Inicio de sesión correcto.", "success")
                return redirect(url_for("dashboard"))
        except Exception:
            pass
        flash("Usuario o contraseña incorrectos.", "danger")
    return render_template("login.html", form=form, nombre_negocio=nombre_negocio)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("login"))


def resumen_sistema():
    result = {}
    for tabla, clave in [("productos","productos"),("clientes","clientes"),
                         ("proveedores","proveedores"),("facturas","facturas")]:
        try:
            result[clave] = ejecutar_sql(f"SELECT COUNT(*) AS total FROM {tabla}", (), True)[0]["total"]
        except Exception:
            result[clave] = 0
    return result


@app.route("/")
def inicio():
    try:
        productos = ejecutar_sql("""SELECT p.*, pr.nombre AS proveedor_nombre
            FROM productos p JOIN proveedores pr ON pr.id_proveedor=p.id_proveedor
            ORDER BY p.id_producto DESC""", (), True)
    except Exception:
        productos = []
    return render_template("index.html", productos=productos, nombre_negocio=nombre_negocio,
                           mensaje_bienvenida=mensaje_bienvenida, resumen=resumen_sistema())


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", nombre_negocio=nombre_negocio, resumen=resumen_sistema())


# ---------------- PRODUCTOS ----------------
def obtener_proveedores():
    return ejecutar_sql("SELECT * FROM proveedores ORDER BY nombre", (), True)


def configurar_proveedores(form):
    form.proveedor.choices = [(p["id_proveedor"], p["nombre"]) for p in obtener_proveedores()]


def obtener_productos():
    return ejecutar_sql("""SELECT p.id_producto,p.nombre,p.categoria,p.precio,p.stock,p.emoji,
        p.id_proveedor,pr.nombre AS proveedor_nombre
        FROM productos p INNER JOIN proveedores pr ON pr.id_proveedor=p.id_proveedor
        ORDER BY p.id_producto DESC""", (), True)


@app.route("/productos")
@login_required
def productos_view():
    return render_template("productos.html", productos=obtener_productos(),
                           delete_form=DeleteForm(), nombre_negocio=nombre_negocio)


@app.route("/productos/nuevo", methods=["GET","POST"])
@login_required
def formulario_producto():
    form = ProductoForm(); configurar_proveedores(form)
    if form.validate_on_submit():
        ejecutar_sql("""INSERT INTO productos
            (nombre,categoria,precio,stock,emoji,id_proveedor)
            VALUES (%s,%s,%s,%s,%s,%s)""",
            (form.nombre.data.strip(),form.categoria.data,form.precio.data,
             form.stock.data,form.emoji.data.strip(),form.proveedor.data))
        flash("Producto creado correctamente en PostgreSQL.", "success")
        return redirect(url_for("productos_view"))
    return render_template("formulario_producto.html",form=form,modo="Registrar",nombre_negocio=nombre_negocio)


@app.route("/productos/editar/<int:producto_id>", methods=["GET","POST"])
@login_required
def editar_producto(producto_id):
    rows = ejecutar_sql("SELECT * FROM productos WHERE id_producto=%s",(producto_id,),True)
    if not rows:
        flash("El producto no existe.","warning"); return redirect(url_for("productos_view"))
    form = ProductoForm(obj=rows[0]); configurar_proveedores(form)
    if not form.is_submitted():
        form.proveedor.data = rows[0]["id_proveedor"]
    if form.validate_on_submit():
        ejecutar_sql("""UPDATE productos SET nombre=%s,categoria=%s,precio=%s,stock=%s,
            emoji=%s,id_proveedor=%s WHERE id_producto=%s""",
            (form.nombre.data.strip(),form.categoria.data,form.precio.data,form.stock.data,
             form.emoji.data.strip(),form.proveedor.data,producto_id))
        flash("Producto actualizado correctamente en PostgreSQL.","success")
        return redirect(url_for("productos_view"))
    return render_template("formulario_producto.html",form=form,modo="Editar",nombre_negocio=nombre_negocio)


@app.post("/productos/eliminar/<int:producto_id>")
@login_required
def eliminar_producto_view(producto_id):
    form=DeleteForm()
    if form.validate_on_submit():
        try:
            ejecutar_sql("DELETE FROM productos WHERE id_producto=%s",(producto_id,))
            flash("Producto eliminado correctamente.","success")
        except Exception:
            flash("No se puede eliminar el producto. Verifica sus relaciones.","danger")
    else:
        flash("Solicitud no válida.","danger")
    return redirect(url_for("productos_view"))


# ---------------- PROVEEDORES ----------------
@app.route("/proveedores")
@login_required
def proveedores_view():
    return render_template("proveedores.html", proveedores=obtener_proveedores(),
                           delete_form=DeleteForm(), nombre_negocio=nombre_negocio)


@app.route("/proveedores/nuevo", methods=["GET","POST"])
@login_required
def formulario_proveedor():
    form=ProveedorForm()
    if form.validate_on_submit():
        ejecutar_sql("INSERT INTO proveedores(nombre,contacto,estado) VALUES(%s,%s,%s)",
                     (form.nombre.data.strip(),form.contacto.data.strip(),form.estado.data))
        flash("Proveedor creado correctamente.","success")
        return redirect(url_for("proveedores_view"))
    return render_template("formulario_proveedor.html",form=form,modo="Registrar",nombre_negocio=nombre_negocio)


@app.route("/proveedores/editar/<int:proveedor_id>", methods=["GET","POST"])
@login_required
def editar_proveedor(proveedor_id):
    rows=ejecutar_sql("SELECT * FROM proveedores WHERE id_proveedor=%s",(proveedor_id,),True)
    if not rows:
        flash("El proveedor no existe.","warning"); return redirect(url_for("proveedores_view"))
    form=ProveedorForm(obj=rows[0])
    if form.validate_on_submit():
        ejecutar_sql("""UPDATE proveedores SET nombre=%s,contacto=%s,estado=%s
            WHERE id_proveedor=%s""",
            (form.nombre.data.strip(),form.contacto.data.strip(),form.estado.data,proveedor_id))
        flash("Proveedor actualizado correctamente.","success")
        return redirect(url_for("proveedores_view"))
    return render_template("formulario_proveedor.html",form=form,modo="Editar",nombre_negocio=nombre_negocio)


@app.post("/proveedores/eliminar/<int:proveedor_id>")
@login_required
def eliminar_proveedor(proveedor_id):
    form=DeleteForm()
    if form.validate_on_submit():
        try:
            ejecutar_sql("DELETE FROM proveedores WHERE id_proveedor=%s",(proveedor_id,))
            flash("Proveedor eliminado correctamente.","success")
        except Exception:
            flash("No se puede eliminar: existen productos relacionados con este proveedor.","danger")
    return redirect(url_for("proveedores_view"))


# ---------------- CLIENTES ----------------
def obtener_clientes():
    return ejecutar_sql("SELECT * FROM clientes ORDER BY id_cliente DESC",(),True)


@app.route("/clientes")
@login_required
def clientes_view():
    return render_template("clientes.html",clientes=obtener_clientes(),
                           delete_form=DeleteForm(),nombre_negocio=nombre_negocio)


@app.route("/clientes/nuevo", methods=["GET","POST"])
@login_required
def formulario_cliente():
    form=ClienteForm()
    if form.validate_on_submit():
        ejecutar_sql("""INSERT INTO clientes(nombre,telefono,correo,estado)
            VALUES(%s,%s,%s,%s)""",
            (form.nombre.data.strip(),form.telefono.data.strip(),form.correo.data.strip().lower(),form.estado.data))
        flash("Cliente creado correctamente en PostgreSQL.","success")
        return redirect(url_for("clientes_view"))
    return render_template("formulario_cliente.html",form=form,modo="Registrar",nombre_negocio=nombre_negocio)


@app.route("/clientes/editar/<int:cliente_id>", methods=["GET","POST"])
@login_required
def editar_cliente(cliente_id):
    rows=ejecutar_sql("SELECT * FROM clientes WHERE id_cliente=%s",(cliente_id,),True)
    if not rows:
        flash("El cliente no existe.","warning"); return redirect(url_for("clientes_view"))
    form=ClienteForm(obj=rows[0])
    if form.validate_on_submit():
        ejecutar_sql("""UPDATE clientes SET nombre=%s,telefono=%s,correo=%s,estado=%s
            WHERE id_cliente=%s""",
            (form.nombre.data.strip(),form.telefono.data.strip(),form.correo.data.strip().lower(),
             form.estado.data,cliente_id))
        flash("Cliente actualizado correctamente.","success")
        return redirect(url_for("clientes_view"))
    return render_template("formulario_cliente.html",form=form,modo="Editar",nombre_negocio=nombre_negocio)


@app.post("/clientes/eliminar/<int:cliente_id>")
@login_required
def eliminar_cliente(cliente_id):
    form=DeleteForm()
    if form.validate_on_submit():
        try:
            ejecutar_sql("DELETE FROM clientes WHERE id_cliente=%s",(cliente_id,))
            flash("Cliente eliminado correctamente.","success")
        except Exception:
            flash("No se puede eliminar el cliente.","danger")
    return redirect(url_for("clientes_view"))


# ---------------- FACTURACIÓN / JOIN ----------------
def configurar_clientes_factura(form):
    form.cliente.choices=[(c["id_cliente"],c["nombre"]) for c in obtener_clientes()]


@app.route("/facturacion")
@login_required
def facturacion_view():
    facturas=ejecutar_sql("""SELECT f.id_factura,f.numero,f.fecha,f.total,f.estado,
        c.nombre AS cliente
        FROM facturas f LEFT JOIN clientes c ON c.id_cliente=f.id_cliente
        ORDER BY f.id_factura DESC""",(),True)
    return render_template("facturacion.html",facturas=facturas,delete_form=DeleteForm(),nombre_negocio=nombre_negocio)


@app.route("/facturacion/nuevo", methods=["GET","POST"])
@login_required
def formulario_facturacion():
    form=FacturacionForm(); configurar_clientes_factura(form)
    if form.validate_on_submit():
        ejecutar_sql("""INSERT INTO facturas(numero,id_cliente,total,estado)
            VALUES(%s,%s,%s,%s)""",
            (form.numero.data.strip().upper(),form.cliente.data,form.total.data,form.estado.data))
        flash("Factura creada correctamente.","success")
        return redirect(url_for("facturacion_view"))
    return render_template("formulario_facturacion.html",form=form,modo="Registrar",nombre_negocio=nombre_negocio)


@app.route("/facturacion/editar/<int:factura_id>", methods=["GET","POST"])
@login_required
def editar_facturacion(factura_id):
    rows=ejecutar_sql("SELECT * FROM facturas WHERE id_factura=%s",(factura_id,),True)
    if not rows:
        flash("La factura no existe.","warning"); return redirect(url_for("facturacion_view"))
    form=FacturacionForm(); configurar_clientes_factura(form)
    if not form.is_submitted():
        f=rows[0]
        form.numero.data=f["numero"]; form.cliente.data=f["id_cliente"]; form.total.data=f["total"]; form.estado.data=f["estado"]
    if form.validate_on_submit():
        ejecutar_sql("""UPDATE facturas SET numero=%s,id_cliente=%s,total=%s,estado=%s
            WHERE id_factura=%s""",
            (form.numero.data.strip().upper(),form.cliente.data,form.total.data,form.estado.data,factura_id))
        flash("Factura actualizada correctamente.","success")
        return redirect(url_for("facturacion_view"))
    return render_template("formulario_facturacion.html",form=form,modo="Editar",nombre_negocio=nombre_negocio)


@app.post("/facturacion/eliminar/<int:factura_id>")
@login_required
def eliminar_facturacion(factura_id):
    form=DeleteForm()
    if form.validate_on_submit():
        ejecutar_sql("DELETE FROM facturas WHERE id_factura=%s",(factura_id,))
        flash("Factura eliminada correctamente.","success")
    return redirect(url_for("facturacion_view"))


@app.context_processor
def estado_postgresql():
    try:
        conectado=probar_conexion()
    except Exception:
        conectado=False
    return {"postgresql_conectado":conectado}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
