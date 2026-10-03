# Ventas Temu

Aplicación web para gestionar pedidos y ventas de productos adquiridos mediante Temu.

## Tecnologías

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Python
- Flask
- Jinja2
- Flask-WTF y WTForms
- Flask-Login
- PostgreSQL

## Funcionalidades

- Página informativa responsive.
- Navegación por Inicio, Quiénes Somos, Productos y Contacto.
- Formulario dinámico con JavaScript.
- Validaciones en tiempo real y al enviar.
- Creación, visualización, conteo y eliminación de registros dinámicos.
- Plantillas Flask con herencia y componentes reutilizables.
- Formularios Flask-WTF con validaciones y protección CSRF.
- Registro e inicio de sesión de usuarios.
- Contraseñas almacenadas mediante hash.
- Sesiones con Flask-Login.
- Rutas administrativas protegidas.
- CRUD de productos, clientes, proveedores y facturación.
- PostgreSQL con claves primarias y foráneas.
- Consultas SELECT, INSERT, UPDATE y DELETE parametrizadas.
- Consultas JOIN para mostrar información relacionada.
- Interfaz responsive con Bootstrap.
- Configuración para despliegue con Gunicorn y Render.

## Estructura

- index.html
- app.py
- models.py
- requirements.txt
- .env.example
- .gitignore
- Procfile
- render.yaml
- conexion/
- forms/
- sql/esquema.sql
- templates/
- templates/components/
- static/css/
- static/js/
- static/img/

## Base de datos

Tablas principales: usuarios, proveedores, productos, clientes y facturas.

Relaciones:
- proveedores → productos
- clientes → facturas

## Configuración

PostgreSQL local:

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=TU_PASSWORD
DB_NAME=ventas_temu
SECRET_KEY=TU_CLAVE_SEGURA

Para PostgreSQL administrado también puede utilizarse DATABASE_URL.
Las credenciales reales deben permanecer fuera del repositorio.

## Ejecución

pip install -r requirements.txt
python app.py

La aplicación utiliza el puerto definido por PORT cuando está desplegada y el puerto 5000 de forma local.