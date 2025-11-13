# ui/clientes/clientes_guardar.py
import flet as ft
from .clientes_db import guardar_cliente_db
from .clientes_utils import limpiar_campos
from .clientes_confirmacion import mostrar_confirmacion

def guardar_cliente_ui(page, conn, razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email, volver_menu):
    from .clientes import mostrar_clientes  # para recargar vista al cargar otro cliente
    
    # Reseteamos colores
    cuit_dni.border_color = ft.Colors.BLACK26
    telefono.border_color = ft.Colors.BLACK26

    error = False
    # Validación CUIT/DNI
    if not cuit_dni.value.isdigit():
        cuit_dni.value = ""
        cuit_dni.border_color = ft.Colors.RED
        error = True

    # Validación teléfono
    if not telefono.value.isdigit():
        telefono.value = ""
        telefono.border_color = ft.Colors.RED
        error = True

    page.update()

    datos = {
        "razon_social": razon_social.value,
        "domicilio": domicilio.value,
        "provincia": provincia.value,
        "localidad": localidad.value,
        "cuit_dni": cuit_dni.value,
        "condicion_iva": condicion_iva.value,
        "telefono": telefono.value,
        "email": email.value
    }

    exito, mensaje = guardar_cliente_db(conn, datos)

    if exito:
        limpiar_campos(
            [razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email],
            page
        )
        mostrar_confirmacion(
            page,
            mensaje,
            volver_menu_func=volver_menu,
            cargar_otro_func=lambda p: mostrar_clientes(p)
        )

    page.update()
