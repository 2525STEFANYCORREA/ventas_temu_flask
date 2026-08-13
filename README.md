# Ventas Temu - Proyecto Integrador Flask

Proyecto de Desarrollo de Aplicaciones Web que integra HTML5, CSS3, Bootstrap, JavaScript, Jinja2 y Flask.

## Estructura

```text
ventas_temu_flask/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── productos.html
│   ├── clientes.html
│   ├── proveedores.html
│   └── facturacion.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
```

## Ejecutar

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

Instalar:
```bash
pip install -r requirements.txt
```

Iniciar:
```bash
python app.py
```

Abrir:
`http://127.0.0.1:5000`

Rutas:
- `/`
- `/productos`
- `/clientes`
- `/proveedores`
- `/facturacion`

## GitHub

```bash
git add .
git commit -m "Proyecto integrador Ventas Temu con Flask"
git push origin main
```

