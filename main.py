# main.py
import flet as ft
from db.init_db import crear_tablas
from menu import menu_principal

def main(page: ft.Page):
    crear_tablas()

    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"
    page.window_width = 800
    page.window_height = 500
    page.window_maximized = False
    page.window_resizable = False

    menu_principal(page)  # arrancamos mostrando el menú

if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)
    #ft.app(target=main, view=ft.WEB_BROWSER, port=8550)