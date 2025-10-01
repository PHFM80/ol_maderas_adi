import flet as ft
from ui.componentes.condiciones.guardar_condiciones import guardar_condiciones
from ui.componentes.funciones.desactivar_boton import desactivar_boton

def condiciones_venta(page):
    # Definir inputs fuera del controls para poder usarlos en on_confirmar_click
    validez_input = ft.TextField(label="Validez de la oferta", expand=True)
    forma_pago_input = ft.TextField(label="Forma de pago", expand=True)
    condicion_pago_input = ft.TextField(label="Condición de pago", expand=True)
    plazo_entrega_input = ft.TextField(label="Plazo de entrega", expand=True)
    lugar_entrega_input = ft.TextField(label="Lugar de entrega", expand=True)
    transporte_input = ft.TextField(label="Transporte", expand=True)

    btn_confirmar = ft.ElevatedButton("Confirmar", bgcolor=ft.Colors.GREEN)

    def on_confirmar_click(e):
        exito = guardar_condiciones(
            validez_input.value,
            forma_pago_input.value,
            condicion_pago_input.value,
            plazo_entrega_input.value,
            lugar_entrega_input.value,
            transporte_input.value
        )
        if exito:
            desactivar_boton(btn_confirmar, page)

    btn_confirmar.on_click = on_confirmar_click



    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Condiciones de Venta", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10),

                ft.Row([
                    validez_input,
                    forma_pago_input,
                    condicion_pago_input,
                ]),
                ft.Row([
                    plazo_entrega_input,
                    lugar_entrega_input,
                    transporte_input,
                ]),

                ft.Divider(height=20),
                ft.Divider(height=20),
                ft.Row([btn_confirmar], alignment=ft.MainAxisAlignment.CENTER),

                
            ],
            spacing=15
        ),
        padding=20,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
    )
