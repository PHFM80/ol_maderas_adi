# app.py
import flet as ft
from ui.formulario import formulario
from db.init_db import crear_tablas  # importa la función que creaste

def main(page: ft.Page):
    crear_tablas()  # ejecuta la creación de la tabla al iniciar

    page.title = "Presupuestos OL Maderas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"
    page.window_width = 800
    page.window_height = 500
    page.window_maximized = False
    page.window_resizable = False

    def on_date_selected(fecha):
        print(f"Fecha seleccionada: {fecha}")

    contenido = formulario(page, on_date_selected)

    page.add(contenido)

if __name__ == "__main__":
    #ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
    ft.app(target=main, view=ft.FLET_APP)

