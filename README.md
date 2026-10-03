# Ventas Temu — Proyecto Integrador

Aplicación web desarrollada con Flask para la gestión de productos, proveedores, clientes y facturación.

## Funcionalidades

- Inicio de sesión y registro de usuarios.
- Autenticación con Flask-Login.
- Protección de páginas administrativas.
- CRUD completo de productos.
- CRUD completo de proveedores.
- CRUD completo de clientes.
- CRUD completo de facturación.
- Relaciones entre tablas mediante claves primarias y foráneas.
- Consultas JOIN para mostrar información relacionada.
- Formularios Flask-WTF con validación y protección CSRF.
- PostgreSQL como base de datos.

## Tablas

1. `usuarios`
2. `proveedores`
3. `productos`
4. `clientes`
5. `facturas`

### Relaciones

- `proveedores.id_proveedor` → `productos.id_proveedor`
- `clientes.id_cliente` → `facturas.id_cliente`

## Estructura del proyecto

```
ventas_temu_flask/
├── app.py
├── models.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── forms/
├── conexion/
├── sql/
├── templates/
└── static/
```

## Tecnologías

- Python
- Flask
- PostgreSQL
- Flask-Login
- Flask-WTF
- WTForms
- psycopg2
- Gunicorn
