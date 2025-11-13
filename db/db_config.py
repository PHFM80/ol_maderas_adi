# db/db_config.py
import sqlite3
import os

# Ruta centralizada de la base de datos
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "presupuesto.db")

def get_connection():
    """
    Devuelve una conexión a la base de datos SQLite.
    """
    return sqlite3.connect(DB_PATH)
