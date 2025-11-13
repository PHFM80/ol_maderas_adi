# ui/clientes/clientes_confirmacion.py
import flet as ft

def mostrar_confirmacion(page: ft.Page, mensaje: str, volver_menu_func, cargar_otro_func):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "Información"

    # Contenedor de mensaje
    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text(mensaje, size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Volver al Menú",
                            on_click=lambda e: volver_menu_func(page),
                            width=180,
                            height=50,
                            bgcolor=ft.Colors.RED_400
                        ),
                        ft.ElevatedButton(
                            "Cargar otro cliente",
                            on_click=lambda e: cargar_otro_func(page),
                            width=180,
                            height=50,
                            bgcolor=ft.Colors.ORANGE_100
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.all(20),
        bgcolor=ft.Colors.BLUE_100,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK26, blur_radius=8, offset=ft.Offset(3, 3))
    )

    page.add(contenedor)
    page.update()
