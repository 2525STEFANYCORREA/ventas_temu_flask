# Ventas Temu — Proyecto Integrador

Aplicación web desarrollada con **Flask, Flask-WTF, Flask-Login y PostgreSQL** para gestionar productos, clientes, proveedores y facturación.

## Requisitos cubiertos

- Flask y estructura organizada del proyecto.
- Plantilla principal `templates/base.html`.
- Herencia Jinja2 con `{% extends "base.html" %}`.
- Componentes reutilizables: `templates/components/navbar.html` y `footer.html`.
- Bootstrap 5 y CSS responsive.
- Formularios Flask-WTF con validaciones y CSRF.
- PostgreSQL como fuente real de datos.
- Conexión centralizada en `conexion/conexion.py`.
- Esquema reproducible en `sql/esquema.sql`.
- Claves primarias y foráneas entre tablas.
- CRUD completo de Productos, Clientes, Proveedores y Facturación.
- Consultas parametrizadas con SELECT, INSERT, UPDATE y DELETE.
- JOIN entre productos/proveedores y facturas/clientes.
- Usuarios almacenados en PostgreSQL.
- Contraseñas protegidas con `generate_password_hash()`.
- Login, logout, `@login_required`, `current_user` y `load_user()`.
- Validaciones dinámicas con JavaScript y Bootstrap en la página principal.
- Archivos CSS, JavaScript e imágenes organizados dentro de `static/`.
- Vista estática en `index.html` para GitHub Pages.

## Estructura

```
ventas_temu_flask/
├── app.py
├── models.py
├── requirements.txt
├── .env.example
├── .gitignore
├── index.html
├── README.md
├── Procfile
├── render.yaml
├── conexion/
│   ├── __init__.py
│   └── conexion.py
├── sql/
│   └── esquema.sql
├── forms/
│   ├── __init__.py
│   ├── login_form.py
│   ├── usuario_form.py
│   ├── producto_form.py
│   ├── cliente_form.py
│   ├── proveedor_form.py
│   └── facturacion_form.py
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
```

## Base de datos

El proyecto utiliza PostgreSQL. La conexión acepta:

- `DATABASE_URL` para servicios administrados.
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` y `DB_NAME` para una instalación local.

El archivo `sql/esquema.sql` permite recrear las tablas:

1. `usuarios`
2. `proveedores`
3. `productos`
4. `clientes`
5. `facturas`

Relaciones principales:

- `productos.id_proveedor` → `proveedores.id_proveedor`
- `facturas.id_cliente` → `clientes.id_cliente`

## Ejecutar localmente

1. Instalar PostgreSQL.
2. Crear la base de datos `ventas_temu`.
3. Crear y activar un entorno virtual.
4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Copiar `.env.example` como `.env` y completar las credenciales locales.
6. Ejecutar `sql/esquema.sql` en PostgreSQL si se desea crear la estructura manualmente.
7. Iniciar Flask:

```bash
python app.py
```

8. Abrir:

```
http://127.0.0.1:5000
```

## Flujo de comprobación

### Productos
- Listar → SELECT
- Registrar → INSERT + commit
- Modificar → UPDATE + WHERE + commit
- Eliminar → DELETE + WHERE + commit

### Autenticación
- Registrar usuario.
- Guardar contraseña mediante hash.
- Iniciar sesión con Flask-Login.
- Proteger módulos con `@login_required`.
- Mostrar el usuario con `current_user`.
- Cerrar sesión con `logout_user()`.

## Seguridad

No se incluyen contraseñas reales ni credenciales de PostgreSQL en el repositorio. El archivo `.env` está excluido mediante `.gitignore`; utiliza `.env.example` como plantilla.

## GitHub Pages

El archivo raíz `index.html` es una **vista estática** del proyecto para la publicación visual. GitHub Pages no ejecuta Python/Flask ni PostgreSQL; la aplicación completa se ejecuta localmente o en un servidor compatible con Flask.

Para publicar la vista estática: **Settings → Pages → Deploy from a branch → main → /(root)**.

## Entrega

- Repositorio: https://github.com/2525STEFANYCORREA/ventas_temu_flask
- Aplicación Flask: ejecución local con PostgreSQL.
- Vista estática: publicación mediante GitHub Pages.

## Autor

**Stefany Leonor Correa Ávila**  
Desarrollo de Aplicaciones Web — 2026


## Checklist final de entrega

- [x] Flask y estructura de proyecto organizada.
- [x] HTML5, CSS3, Bootstrap y JavaScript conservados para los avances iniciales.
- [x] Jinja2 con `base.html`, `{% extends %}`, `{% include %}`, variables, `for` e `if/else`.
- [x] Formularios Flask-WTF con validaciones, GET/POST, `validate_on_submit()` y CSRF.
- [x] PostgreSQL configurado mediante `conexion/conexion.py`.
- [x] Cinco tablas: `usuarios`, `proveedores`, `productos`, `clientes` y `facturas`.
- [x] Claves primarias y claves foráneas.
- [x] CRUD completo con consultas parametrizadas.
- [x] JOIN entre productos/proveedores y facturas/clientes.
- [x] Login, registro, hash de contraseñas, sesión, `@login_required` y logout.
- [x] `requirements.txt` actualizado.
- [x] `render.yaml` preparado para Flask + PostgreSQL + Gunicorn.
- [x] `.env` excluido del repositorio; se conserva `.env.example`.
- [x] `index.html` raíz preparado como evidencia estática de los avances HTML/CSS/JS.

### Prueba final que debe realizarse antes de entregar

Con PostgreSQL activo, ejecutar:

**Registro → Login → Listar → Agregar → Modificar → Eliminar → JOIN → Cerrar sesión.**

También comprobar que una ruta protegida no sea accesible sin iniciar sesión y que los cambios realizados en PostgreSQL permanezcan después de reiniciar Flask.

> Nota: el código y la estructura del repositorio pueden revisarse desde GitHub, pero la prueba real de PostgreSQL y el funcionamiento público de Render deben comprobarse con la base de datos y el servicio desplegado activos.
