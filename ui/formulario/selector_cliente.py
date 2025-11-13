# ui/formulario/selector_cliente.py
import sqlite3
import flet as ft

def selector_cliente(conn):
    """
    Devuelve una lista de ft.dropdown.Option para el dropdown de clientes.
    Cada opción muestra 'razon_social - cuit_dni' y la key es el id_cliente.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id_cliente, razon_social, cuit_dni FROM clientes ORDER BY razon_social")
    clientes = cursor.fetchall()
    cursor.close()

    opciones = [
        ft.dropdown.Option(key=str(cliente[0]), text=f"{cliente[1]} - {cliente[2]}")
        for cliente in clientes
    ]
    return opciones
