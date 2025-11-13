# ui/previsualizacion/alerta_conclusion.py
import flet as ft

def mostrar_alerta(page: ft.Page, mensaje: str):
    from menu import menu_principal
    page.controls.clear()

    # Contenedor interno con mensaje y botón
    contenedor_interno = ft.Column(
        [
            ft.Text(mensaje, size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900, text_align=ft.TextAlign.CENTER),
            ft.ElevatedButton(
                "Aceptar",
                width=200,
                height=50,
                bgcolor=ft.Colors.GREEN_400,
                on_click=lambda e: menu_principal(page)
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )

    # Contenedor principal que ocupa toda la pantalla
    contenedor_principal = ft.Container(
        content=contenedor_interno,
        expand=True,
        alignment=ft.alignment.center
    )

    page.add(contenedor_principal)
    page.update()
