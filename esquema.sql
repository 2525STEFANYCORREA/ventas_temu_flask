-- Ventas Temu - Semana 15
-- PostgreSQL
-- Tablas relacionadas:
-- proveedores 1:N productos
-- clientes 1:N facturas

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(150) NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Activo'
);

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cedula VARCHAR(20),
    telefono VARCHAR(20),
    correo VARCHAR(120),
    estado VARCHAR(20) NOT NULL DEFAULT 'Activo'
);

CREATE TABLE IF NOT EXISTS productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(60) NOT NULL,
    precio NUMERIC(10,2) NOT NULL CHECK (precio > 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    emoji VARCHAR(10) NOT NULL,
    id_proveedor INTEGER NOT NULL,
    CONSTRAINT fk_producto_proveedor FOREIGN KEY (id_proveedor)
        REFERENCES proveedores(id_proveedor)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS facturas (
    id_factura SERIAL PRIMARY KEY,
    numero VARCHAR(20) UNIQUE NOT NULL,
    id_cliente INTEGER,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10,2) NOT NULL CHECK (total > 0),
    estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
    CONSTRAINT fk_factura_cliente FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO proveedores (nombre, contacto, estado)
SELECT 'Temu Marketplace', 'Atención en línea', 'Activo'
WHERE NOT EXISTS (SELECT 1 FROM proveedores WHERE nombre = 'Temu Marketplace');

INSERT INTO proveedores (nombre, contacto, estado)
SELECT 'Distribuciones Ecuador', 'Pedidos y logística', 'Activo'
WHERE NOT EXISTS (SELECT 1 FROM proveedores WHERE nombre = 'Distribuciones Ecuador');

INSERT INTO clientes (nombre, cedula, telefono, correo, estado)
SELECT 'María López', '0900000001', '099 111 2233', 'maria@email.com', 'Activo'
WHERE NOT EXISTS (SELECT 1 FROM clientes WHERE correo = 'maria@email.com');

INSERT INTO clientes (nombre, cedula, telefono, correo, estado)
SELECT 'Carlos Zambrano', '0900000002', '098 222 3344', 'carlos@email.com', 'Activo'
WHERE NOT EXISTS (SELECT 1 FROM clientes WHERE correo = 'carlos@email.com');
