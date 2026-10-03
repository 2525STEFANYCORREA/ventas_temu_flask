# Ventas Temu — Proyecto Integrador Semana 15

Aplicación Flask para el proyecto **Ventas Temu**, actualizada desde la Semana 14 para trabajar con **PostgreSQL** e implementar CRUD completo.

## Implementaciones de la Semana 15

- PostgreSQL como base de datos.
- Login y registro con Flask-Login.
- Páginas administrativas protegidas con `@login_required`.
- CRUD completo: **Crear, Leer, Actualizar y Eliminar**.
- Formularios Flask-WTF con validaciones y protección CSRF.
- Consultas SQL parametrizadas.
- Relaciones mediante `PRIMARY KEY` y `FOREIGN KEY`.
- Consultas `JOIN` para mostrar información relacionada.
- `requirements.txt` actualizado con `psycopg2-binary` y `gunicorn`.
- Configuración preparada para deploy en Render.
- Variables de entorno compatibles con `DATABASE_URL` de Render.

## Tablas y relaciones

La base contiene cinco tablas:

1. `usuarios` — login.
2. `proveedores` — información de proveedores.
3. `productos` — catálogo de productos.
4. `clientes` — información de clientes.
5. `facturas` — facturación.

Relaciones:

- `proveedores.id_proveedor` → `productos.id_proveedor`
- `clientes.id_cliente` → `facturas.id_cliente`

Por lo tanto existen más de tres tablas relacionadas y se utilizan claves primarias y foráneas.

## CRUD

### Productos
- `SELECT` para listar.
- `INSERT` para crear.
- `UPDATE` para editar.
- `DELETE` para eliminar.
- `INNER JOIN` con proveedores.

### Clientes
- `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

### Proveedores
- `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

### Facturación
- `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- `LEFT JOIN` con clientes para consultar información relacionada.

## Estructura principal

```text
ventas_temu_flask/
├── app.py
├── models.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── forms/
├── conexion/
│   └── conexion.py
├── sql/
│   └── esquema.sql
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── login.html
│   ├── registro.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   └── facturacion.html
└── static/
    ├── style.css
    ├── script.js
    └── logo.svg
```

## Ejecutar localmente

1. Instalar PostgreSQL.
2. Crear la base `ventas_temu`.
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:

```text
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=tu_clave
DB_NAME=ventas_temu
DB_SSLMODE=prefer
SECRET_KEY=una_clave_segura
```

5. Ejecutar:

```bash
python app.py
```

6. Abrir:

```text
http://localhost:5000
```

La aplicación crea las tablas automáticamente cuando puede conectarse a PostgreSQL. También se incluye `sql/esquema.sql` para ejecutar el esquema manualmente.

## Deploy en Render

El proyecto incluye `render.yaml`.

En Render se puede crear el servicio web y la base PostgreSQL desde el Blueprint. La aplicación utiliza `DATABASE_URL` cuando está disponible.

Configuración del Web Service:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Variable: `DATABASE_URL`
- Variable: `SECRET_KEY`

Si se configura el servicio manualmente, se debe conectar la base PostgreSQL y copiar su URL de conexión en `DATABASE_URL`.

## Prueba obligatoria

Realizar en la aplicación publicada:

**Login → Listar → Agregar → Modificar → Eliminar → consultar información relacionada → Cerrar sesión**

### Evidencias recomendadas para el informe

1. Login funcionando.
2. Panel administrativo protegido.
3. Listado de productos.
4. Producto agregado.
5. Producto modificado.
6. Producto eliminado.
7. Proveedor relacionado con producto mediante JOIN.
8. Cliente relacionado con factura mediante JOIN.
9. PostgreSQL conectado.
10. Aplicación publicada en Render.
11. Repositorio GitHub actualizado.


## Evaluación final — Semana de cierre

### Orden recomendado para la demostración en video

1. Mostrar la página principal y la navegación.
2. Entrar a **Login** e iniciar sesión con un usuario registrado.
3. Mostrar el **Dashboard** y explicar que las rutas administrativas están protegidas con `@login_required`.
4. Entrar a **Productos** y mostrar los registros existentes.
5. Crear un producto seleccionando un proveedor.
6. Editar el producto creado.
7. Mostrar la columna **Proveedor** para evidenciar la relación mediante `JOIN`.
8. Eliminar el producto y comprobar que desaparece de la lista.
9. Entrar a **Clientes** y realizar una operación CRUD.
10. Entrar a **Facturación** y mostrar que la consulta relaciona la factura con el cliente mediante `LEFT JOIN`.
11. Mostrar **Proveedores** y explicar la relación `proveedores → productos`.
12. Cerrar sesión y comprobar que el sistema regresa al login.

### Guion breve para explicar el proyecto

> Mi proyecto se denomina **Ventas Temu** y fue desarrollado con Flask. El sistema permite gestionar productos, proveedores, clientes y facturas. Cuenta con autenticación de usuarios mediante Flask-Login y las áreas administrativas están protegidas. La información se almacena en PostgreSQL y se utilizan claves primarias y foráneas para relacionar las tablas.
>
> En productos se puede crear, consultar, modificar y eliminar información. Cada producto está relacionado con un proveedor. En facturación, cada registro puede estar relacionado con un cliente y la aplicación utiliza consultas JOIN para mostrar esa información en una misma tabla. Los formularios utilizan Flask-WTF y las operaciones SQL utilizan parámetros para evitar construir consultas con datos directamente concatenados.
>
> Finalmente, se verifica el flujo completo: inicio de sesión, consulta, creación, modificación, eliminación, consulta de información relacionada y cierre de sesión.

### Evidencias que conviene guardar

- Captura del login.
- Captura del dashboard.
- Captura del listado de productos.
- Captura de producto creado.
- Captura de producto modificado.
- Captura después de eliminar.
- Captura del JOIN producto-proveedor.
- Captura de clientes y facturación.
- Captura de PostgreSQL con las tablas y relaciones.
- Captura del repositorio GitHub.
- Captura de la aplicación funcionando en Render.
- Enlace del video de demostración.

### Entrega

La plataforma debe recibir el **enlace del repositorio GitHub** y el **enlace del video** publicado en YouTube o disponible en el repositorio, según indique el docente.
