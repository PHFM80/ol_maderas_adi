# ui\componentes\funciones\desactivar_boton.py

import flet as ft

def desactivar_boton(boton, page):
    boton.bgcolor = ft.Colors.GREY_500
    boton.disabled = True
    page.update()
