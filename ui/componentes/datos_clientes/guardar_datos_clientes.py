# ui\componentes\datos_clientes\guardar_datos_clientes.py

import sqlite3
import os

def guardar_datos_clientes(
    razon_social,
    domicilio,
    provincia,
    localidad,
    cuit,
    condicion_iva,
    telefono,
    email
):
    # Ruta correcta hacia la base de datos
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../../../db/presupuesto.db")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO datos_cliente (
                razon_social,
                domicilio,
                provincia,
                localidad,
                cuit_dni,
                condicion_iva,
                telefono,
                email
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            razon_social,
            domicilio,
            provincia,
            localidad,
            cuit,
            condicion_iva,
            telefono,
            email
        ))
        conn.commit()
        conn.close()
        print("✔ Datos del cliente guardados correctamente.")
    except Exception as e:
        print(f"⚠ Error al guardar datos del cliente: {e}")
