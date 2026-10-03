# Ventas Temu

Aplicación web desarrollada con Flask y PostgreSQL para la gestión de productos, clientes, proveedores y facturación.

## Tecnologías

- Flask
- Flask-WTF y WTForms
- Flask-Login
- PostgreSQL
- Jinja2
- Bootstrap 5
- HTML5, CSS3 y JavaScript

## Funcionalidades

- Registro e inicio de sesión de usuarios.
- Autenticación y cierre de sesión.
- Rutas protegidas mediante autenticación.
- CRUD completo de productos.
- CRUD completo de clientes.
- CRUD completo de proveedores.
- CRUD completo de facturación.
- Formularios validados con Flask-WTF y protección CSRF.
- Cinco tablas relacionadas mediante claves primarias y foráneas.
- Consultas SQL parametrizadas.
- Consultas JOIN para mostrar relaciones entre registros.
- Navegación funcional e interfaz responsive.

## Estructura

```
ventas_temu_flask/
├── app.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile
├── render.yaml
├── conexion/
│   ├── __init__.py
│   └── conexion.py
├── forms/
│   ├── __init__.py
│   ├── login_form.py
│   ├── usuario_form.py
│   ├── producto_form.py
│   ├── cliente_form.py
│   ├── proveedor_form.py
│   └── facturacion_form.py
├── sql/
│   └── esquema.sql
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── registro.html
│   ├── dashboard.html
│   ├── productos.html
│   ├── formulario_producto.html
│   ├── clientes.html
│   ├── formulario_cliente.html
│   ├── proveedores.html
│   ├── formulario_proveedor.html
│   ├── facturacion.html
│   ├── formulario_facturacion.html
│   └── components/
│       ├── navbar.html
│       └── footer.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
        └── logo.svg
```

## Base de datos

Las tablas principales son:

- `usuarios`
- `proveedores`
- `productos`
- `clientes`
- `facturas`

Relaciones:

- Proveedores 1:N Productos.
- Clientes 1:N Facturas.
