# ui\componentes\elementos_tabla\guardar_detalle_producto.py

import sqlite3
import os

def guardar_detalle_en_bd(cantidad, descripcion, precio_unitario, total):
    try:
        total = round(cantidad * precio_unitario, 2)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "../../../db/presupuesto.db")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO detalle_producto (
                cantidad,
                descripcion,
                precio_unitario,
                total
            ) VALUES (?, ?, ?, ?)
        """, (
            cantidad,
            descripcion,
            precio_unitario,
            total
        ))

        conn.commit()
        conn.close()
        print("✔ Producto guardado correctamente.")

    except Exception as e:
        print(f"⚠ Error al guardar producto: {e}")
