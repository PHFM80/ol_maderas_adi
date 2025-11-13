# db\init_db.py

import sqlite3
import os

def crear_tablas():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "presupuesto.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Tabla clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            razon_social TEXT,
            domicilio TEXT,
            provincia TEXT,
            localidad TEXT,
            cuit_dni INTERGER,
            condicion_iva TEXT,
            telefono interger,
            email TEXT
        )
    """)

    # Tabla presupuestos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS presupuestos (
            id_presupuesto INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            fecha TEXT,
            moneda TEXT,
            validez_oferta TEXT,
            forma_pago TEXT,
            condicion_pago TEXT,
            plazo_entrega TEXT,
            lugar_entrega TEXT,
            transporte TEXT,
            subtotal REAL,
            descuento_porcentaje REAL,
            descuento_valor REAL,
            iva_105 REAL,
            iva_21 REAL,
            total_final REAL,
            total_letras TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        )
    """)

    # Tabla items del presupuesto
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            id_presupuesto INTEGER,
            cantidad INTEGER,
            descripcion TEXT,
            precio_unitario REAL,
            total REAL,
            FOREIGN KEY (id_presupuesto) REFERENCES presupuestos(id_presupuesto)
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    crear_tablas()

