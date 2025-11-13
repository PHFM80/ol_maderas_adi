# ui/pdf/buscar_x_id.py 

import sqlite3
import os

def obtener_cliente_por_id(id_cliente):
    """
    Obtiene los datos completos de un cliente desde la base de datos SQLite.
    
    :param id_cliente: str o int con el ID del cliente
    :return: dict con campos que necesita la plantilla HTML
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # hasta la carpeta del proyecto
    db_path = os.path.join(base_dir, "db", "presupuesto.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT razon_social, cuit_dni as cuit, domicilio, provincia, localidad, telefono, email, condicion_iva
        FROM clientes
        WHERE id_cliente = ?
    """, (id_cliente,))
    
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return {
            "razon_social": resultado[0],
            "cuit": resultado[1],
            "domicilio": resultado[2],
            "provincia": resultado[3],
            "localidad": resultado[4],
            "telefono": resultado[5],
            "email": resultado[6],
            "condicion_iva": resultado[7],
        }
    else:
        # Retorna un diccionario vacío con las claves para que la plantilla no rompa
        return {
            "razon_social": "",
            "cuit": "",
            "domicilio": "",
            "provincia": "",
            "localidad": "",
            "telefono": "",
            "email": "",
            "condicion_iva": "",
        }
