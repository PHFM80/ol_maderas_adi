# db\init_db.py

import sqlite3
import os

def crear_tablas():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "presupuesto.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encabezado (
            nro_presupuesto INTEGER,
            fecha TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datos_cliente (
            razon_social TEXT,
            domicilio TEXT,
            provincia TEXT,
            localidad TEXT,
            cuit_dni TEXT,
            condicion_iva TEXT,
            telefono TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detalle_producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER,
            descripcion TEXT,
            precio_unitario REAL,
            total REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moneda (
            moneda TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS condiciones_venta (
            validez_oferta TEXT,
            forma_pago TEXT,
            condicion_pago TEXT,
            plazo_entrega TEXT, 
            lugar_entrega TEXT,
            transporte TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS valores_presupuesto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subtotal REAL,
            descuento_porcentaje REAL,
            descuento_valor REAL,
            iva_105 REAL,
            iva_21 REAL,
            total_final REAL,
            total_letras TEXT
        )
    """)


    conn.commit()
    conn.close()



if __name__ == "__main__":
    crear_tablas()

