# utils\f_cerrar_app.py
import flet as ft

def cerrar_app(page: ft.Page):
    # Limpiar toda la UI
    page.controls.clear()

    # Mostrar mensaje de despedida
    mensaje = ft.Text(
        "El PDF se generó correctamente.\nGracias por usar la app de generacion de presupuesto.\nApp desarrollada por Pablo Flores.\nD & T\npablofloresmaza@gmail.com",
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    contenedor = ft.Container(
        content=mensaje,
        alignment=ft.alignment.center,
        expand=True
    )

    page.controls.append(contenedor)
    page.update()
