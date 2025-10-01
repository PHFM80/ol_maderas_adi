# ui\componentes\encabezado\guardar_encabezado_bd.py

import sqlite3
import os

def guardar_encabezado_en_bd(nro_presupuesto, fecha):
    # Ruta relativa a la base de datos
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../../../db/presupuesto.db")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO encabezado (nro_presupuesto, fecha) VALUES (?, ?)",
            (nro_presupuesto, fecha)
        )

        conn.commit()
        conn.close()
        print(f"✔ Datos guardados: {nro_presupuesto}, {fecha}")

    except Exception as e:
        print(f"⚠ Error al guardar en la base de datos: {e}")
