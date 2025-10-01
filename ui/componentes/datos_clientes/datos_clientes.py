import flet as ft
from ui.componentes.funciones.desactivar_boton import desactivar_boton
from ui.componentes.datos_clientes.guardar_datos_clientes import guardar_datos_clientes

def vista_datos_clientes(page):
    # Campos para capturar valores
    razon_social = ft.TextField(label="Razón Social", width=400)
    domicilio = ft.TextField(label="Domicilio", width=400)
    provincia = ft.TextField(label="Provincia", width=400)
    localidad = ft.TextField(label="Localidad", width=400)
    cuit_dni = ft.TextField(label="CUIT / DNI", width=400)

    condicion_iva = ft.Dropdown(
        label="Condición IVA",
        width=400,
        options=[
            ft.dropdown.Option("Consumidor Final"),
            ft.dropdown.Option("Responsable Inscripto"),
            ft.dropdown.Option("Responsable No Inscripto"),
            ft.dropdown.Option("Exento"),
        ],
        value=None,
    )

    telefono = ft.TextField(label="Teléfono", width=400)
    email = ft.TextField(label="Email", width=400)

    def confirmar_click(e):
        guardar_datos_clientes(
            razon_social.value,
            domicilio.value,
            provincia.value,
            localidad.value,
            cuit_dni.value,
            condicion_iva.value,
            telefono.value,
            email.value,
        )
        desactivar_boton(e.control, page)
        print("Datos del cliente guardados.")

    boton_confirmar = ft.ElevatedButton(
        "Confirmar",
        icon=ft.Icons.CHECK,
        bgcolor=ft.Colors.GREEN,
        on_click=confirmar_click,
    )

    return ft.Container(
        content=ft.Column([
            ft.Text("Datos del Cliente", size=20, weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        razon_social,
                        domicilio,
                        provincia,
                        localidad,
                    ]),
                    expand=True
                ),
                ft.Container(
                    content=ft.Column([
                        cuit_dni,
                        condicion_iva,
                        telefono,
                        email,
                    ]),
                    expand=True
                ),
            ]),
            ft.Container(height=20),
            ft.Row([boton_confirmar], alignment=ft.MainAxisAlignment.CENTER)
        ]),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        border=ft.border.all(1, ft.Colors.GREY_300),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=4,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(2, 2),
        ),
    )
