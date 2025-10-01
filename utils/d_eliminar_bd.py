# utils\d_eliminar_bd.py
import os

def eliminar_base_de_datos():
    archivo_db = os.path.join(os.path.dirname(__file__), "../db/presupuesto.db")
    archivo_db = os.path.normpath(archivo_db)

    if os.path.exists(archivo_db):
        os.remove(archivo_db)
