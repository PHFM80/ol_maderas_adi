import flet as ft
import locale

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

def formatear_moneda(valor):
    return "$ " + locale.format_string("%.2f", valor, grouping=True).replace(".", "X").replace(",", ".").replace("X", ",")

def crear_tabla_items(items):
    tabla_items = [
        ft.Row(
            [
                ft.Text("N°", weight=ft.FontWeight.BOLD, width=30),
                ft.Text("Descripción", weight=ft.FontWeight.BOLD, width=300),
                ft.Text("Cantidad", weight=ft.FontWeight.BOLD, width=90),
                ft.Text("Precio Unitario", weight=ft.FontWeight.BOLD, width=140),
                ft.Text("Total", weight=ft.FontWeight.BOLD, width=120)
            ],
            spacing=10
        )
    ]

    for idx, item in enumerate(items, start=1):
        fila = ft.Row(
            [
                ft.Text(str(idx), width=30),
                ft.Text(item["descripcion"], width=300),
                ft.Text(str(item["cantidad"]), width=90),
                ft.Text(formatear_moneda(item["precio_unitario"]), width=140),
                ft.Text(formatear_moneda(item["total"]), width=120)
            ],
            spacing=10
        )
        tabla_items.append(fila)

    contenedor = ft.Container(
        content=ft.Column([ft.Text("Ítems:", size=20, weight=ft.FontWeight.BOLD)] + tabla_items),
        padding=20,
        width=800,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor
