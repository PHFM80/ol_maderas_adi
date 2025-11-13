# ui/clientes/clientes_buscar.py
import flet as ft
from .clientes_db import buscar_cliente

def buscar_cliente_ui(page, conn, razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email):
    """
    Busca un cliente en la base de datos usando la conexión pasada.
    Actualiza los campos si se encuentra, muestra SnackBar si no.
    """
    cliente = buscar_cliente(conn, razon_social.value, cuit_dni.value)
    if cliente:
        razon_social.value, domicilio.value, provincia.value, localidad.value, cuit_dni.value, condicion_iva.value, telefono.value, email.value = \
            cliente[1], cliente[2], cliente[3], cliente[4], str(cliente[5]), cliente[6], str(cliente[7]), cliente[8]
    else:
        page.snack_bar = ft.SnackBar(ft.Text("Cliente no encontrado"), open=True, duration=3000)
    page.update()
