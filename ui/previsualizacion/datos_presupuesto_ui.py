# ui/previsualizacion/datos_presupuesto_ui.py
import flet as ft
from db.db_config import get_connection

def crear_contenedor_datos(datos_presupuesto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT razon_social, domicilio, provincia, localidad, cuit_dni, condicion_iva, telefono, email "
        "FROM clientes WHERE id_cliente = ?", 
        (datos_presupuesto["id_cliente"],)
    )
    cliente_data = cursor.fetchone()
    conn.close()

    if cliente_data:
        cliente_texto = f"""
{cliente_data[0]}
Domicilio: {cliente_data[1]}, {cliente_data[3]}, {cliente_data[2]}
CUIT/DNI: {cliente_data[4]}
Condición IVA: {cliente_data[5]}
Teléfono: {cliente_data[6]}
Email: {cliente_data[7]}
"""
    else:
        cliente_texto = "Cliente no encontrado"

    datos_column = ft.Column(
        [
            ft.Text(f"Nro Presupuesto: {datos_presupuesto['numero_presupuesto']}", size=18),
            ft.Text(f"Fecha: {datos_presupuesto['fecha']}", size=18),
            ft.Text("Cliente:", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(cliente_texto, size=16),
            ft.Text(f"Moneda: {datos_presupuesto['moneda']}", size=18),
            ft.Divider(thickness=1)
        ],
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

    contenedor = ft.Container(
        content=datos_column,
        padding=20,
        width=800,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )

    return contenedor
