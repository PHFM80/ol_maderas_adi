# ui/clientes/clientes.py
import flet as ft
from .clientes_ui import crear_campos
from .clientes_buscar import buscar_cliente_ui
from .clientes_guardar import guardar_cliente_ui
from db.db_config import get_connection  # usamos la función para obtener conexión

def mostrar_clientes(page: ft.Page):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "OL Maderas - Clientes"

    # Crear campos
    razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email = crear_campos()

    # Función de navegación
    def volver_menu(e):
        from menu import menu_principal
        menu_principal(page)

    # Función buscar cliente
    def buscar(e):
        conn = get_connection()
        buscar_cliente_ui(page, conn, razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email)
        conn.close()

    # Función guardar cliente
    def guardar(e):
        conn = get_connection()
        guardar_cliente_ui(page, conn, razon_social, cuit_dni, domicilio, provincia, localidad, condicion_iva, telefono, email, volver_menu)
        conn.close()

    # Título igual que menú principal
    titulo = ft.Container(
        content=ft.Text(
            "Gestión de Clientes",
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

    # Botones
    boton_style = ft.ButtonStyle(text_style=ft.TextStyle(size=22))
    botones_guardar = ft.Column(
        [
            ft.ElevatedButton("Guardar", on_click=guardar, width=220, height=50, bgcolor=ft.Colors.ORANGE_100, style=boton_style),
            ft.ElevatedButton("Volver al Menú", on_click=volver_menu, width=220, height=50, bgcolor=ft.Colors.RED_400, style=boton_style),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=25,
    )

    # Fila buscador
    buscador = ft.Row(
        [razon_social, cuit_dni, ft.ElevatedButton("Buscar", on_click=buscar, width=120, height=40)],
        spacing=15, alignment=ft.MainAxisAlignment.CENTER
    )

    # Campos restantes
    campos = ft.Column([domicilio, provincia, localidad, condicion_iva, telefono, email], spacing=15)

    # Layout principal
    page.add(
        ft.Column(
            [titulo, buscador, campos, botones_guardar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30
        )
    )

    page.update()
