# ui/componentes/generar_pdf/generar_pdf.py

import flet as ft
from utils.pdf_generator import pdf_generator

def generar_pdf(page):
    texto_aviso = ft.Text(
        "Asegúrese de que los datos ingresados son correctos antes de:",
        size=16,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    btn_generar = ft.ElevatedButton(
        "Generar PDF",
        bgcolor=ft.Colors.BLUE,
        on_click=lambda e: pdf_generator(page),
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                texto_aviso,
                ft.Divider(height=10),
                ft.Row([btn_generar], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
    )
