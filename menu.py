# menu.py 
import flet as ft
from ui.formulario import formulario
from ui.clientes import clientes
from ui.consultas import consultas

def menu_principal(page: ft.Page):
    page.title = "OL Maderas - Menú Principal"
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300  # fondo suave

    # Funciones de navegación
    def abrir_clientes(e):
        page.controls.clear()
        clientes.mostrar_clientes(page)

    def abrir_presupuestos(e):
        page.controls.clear()
        formulario.mostrar_formulario(page)

    def abrir_consultas(e):
        page.controls.clear()
        consultas.mostrar_consultas(page)

    def salir(e):
        page.window.destroy()

    # Título elegante
    titulo = ft.Container(
        content=ft.Text(
            "Menú del generador de presupuestos",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_900
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.symmetric(vertical=25, horizontal=30),
        bgcolor=ft.Colors.BLUE_100,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(
            color=ft.Colors.BLACK26,
            blur_radius=8,
            offset=ft.Offset(3,3)
        ),
    )

    # Botones centrados y separados
    boton_style = ft.ButtonStyle(
        text_style=ft.TextStyle(size=22)  # tamaño de letra ajustado
    )
    botones = ft.Column(
        [
            ft.ElevatedButton("Clientes", on_click=abrir_clientes, width=220, height=50,bgcolor=ft.Colors.ORANGE_100, style=boton_style),
            ft.ElevatedButton("Presupuestos", on_click=abrir_presupuestos, width=220, height=50,bgcolor=ft.Colors.GREEN_100, style=boton_style),
            ft.ElevatedButton("Consultas", on_click=abrir_consultas, width=220, height=50, bgcolor=ft.Colors.BLUE_100, style=boton_style),
            ft.ElevatedButton("Salir", on_click=salir, width=220, height=50, bgcolor=ft.Colors.RED_400, style=boton_style),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25,  # separación vertical
    )

    # Contenedor principal centrado
    page.add(
        ft.Column(
            [titulo, botones],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )
    )

    page.update()
