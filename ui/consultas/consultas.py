# ui/consultas/consultas.py

import flet as ft
from . import reimpresion_menu

def mostrar_consultas(page: ft.Page):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "OL Maderas - Consultas"

    # Funciones de navegación interna
    def abrir_reimpresion(e):
        reimpresion_menu.mostrar_reimpresion(page)

    def volver_menu(e):
        from menu import menu_principal
        menu_principal(page)

    # Título principal
    titulo = ft.Container(
        content=ft.Text(
            "Menú de Consultas",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_900
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.symmetric(vertical=25, horizontal=30),
        bgcolor=ft.Colors.BLUE_100,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK26, blur_radius=8, offset=ft.Offset(3,3)),
    )

    # Botones
    boton_style = ft.ButtonStyle(text_style=ft.TextStyle(size=22))
    botones = ft.Column(
        [
            ft.ElevatedButton(
                "Reimprimir Presupuesto",
                on_click=abrir_reimpresion,
                width=300,
                height=50,
                bgcolor=ft.Colors.GREEN_100,
                style=boton_style
            ),
            # Aquí se pueden agregar más botones para otras consultas
            ft.ElevatedButton(
                "Volver al Menú",
                on_click=volver_menu,
                width=300,
                height=50,
                bgcolor=ft.Colors.RED_400,
                style=boton_style
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25
    )

    page.add(ft.Column([titulo, botones], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50))
    page.update()
