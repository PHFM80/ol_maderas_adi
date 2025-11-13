#ui/clientes/clientes_ui.py
import flet as ft

def crear_campos():
    """
    Crea y retorna todos los campos de la vista de clientes.
    """
    razon_social = ft.TextField(label="Razón Social", width=300)
    cuit_dni = ft.TextField(label="CUIT/DNI (todo seguido y sin puntos)", width=300)
    domicilio = ft.TextField(label="Domicilio", width=300)
    provincia = ft.TextField(label="Provincia", width=300)
    localidad = ft.TextField(label="Localidad", width=300)
    condicion_iva = ft.Dropdown(
        label="Condición IVA",
        width=300,
        options=[
            ft.dropdown.Option("Consumidor final"),
            ft.dropdown.Option("Responsable inscripto"),
            ft.dropdown.Option("Responsable no inscripto"),
            ft.dropdown.Option("Monotributista"),
            ft.dropdown.Option("Exento"),
        ]
    )
    telefono = ft.TextField(label="Teléfono (ej.:261778899)", width=300)
    email = ft.TextField(label="Email", width=300)
    return razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email
