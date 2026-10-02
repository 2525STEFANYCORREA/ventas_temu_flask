import os
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import Error


def obtener_conexion():
    """Crea una conexión PostgreSQL usando DATABASE_URL (Render) o variables DB_*."""
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        # Render/servicios gestionados suelen aceptar SSL para conexiones externas.
        sslmode = os.environ.get("DB_SSLMODE", "require")
        return psycopg2.connect(database_url, sslmode=sslmode)

    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.environ.get("DB_PORT", "5432")),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", ""),
        dbname=os.environ.get("DB_NAME", "ventas_temu"),
    )


def probar_conexion():
    conn = None
    try:
        conn = obtener_conexion()
        return True
    except Error:
        return False
    finally:
        if conn:
            conn.close()


def ejecutar_sql(sql, parametros=(), fetch=False, many=False):
    """Ejecuta SQL parametrizado y cierra recursos."""
    conn = None
    try:
        conn = obtener_conexion()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            if many:
                cursor.executemany(sql, parametros)
                resultado = None
            else:
                cursor.execute(sql, parametros)
                resultado = cursor.fetchall() if fetch else None
        conn.commit()
        return resultado
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()
