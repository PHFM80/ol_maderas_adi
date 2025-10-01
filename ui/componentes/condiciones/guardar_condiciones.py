# ui/componentes/condiciones/guardar_condiciones.py

import sqlite3
import os

def guardar_condiciones(validez_oferta, forma_pago, condicion_pago, plazo_entrega, lugar_entrega, transporte):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../db/presupuesto.db")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM condiciones_venta")

        cursor.execute("""
            INSERT INTO condiciones_venta (
                validez_oferta,
                forma_pago,
                condicion_pago,
                plazo_entrega,
                lugar_entrega,
                transporte
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (validez_oferta, forma_pago, condicion_pago, plazo_entrega, lugar_entrega, transporte))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al guardar condiciones de venta: {e}")
        return False
