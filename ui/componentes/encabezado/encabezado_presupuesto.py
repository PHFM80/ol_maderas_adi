# ui/componentes/encabezado/encabezado_presupuesto.py

import flet as ft
from ui.componentes.encabezado.selector_fecha import SelectorFecha
from ui.componentes.encabezado.nuevo_nro_presup import obtener_nuevo_numero
from ui.componentes.encabezado.guardar_encabezado_bd import guardar_encabezado_en_bd
from ui.componentes.funciones.desactivar_boton import desactivar_boton


def EncabezadoPresupuesto(page, on_date_selected):
    nro_presupuesto = obtener_nuevo_numero()

    campo_nro = ft.TextField(
        label="N° Presupuesto",
        value=str(nro_presupuesto),
        width=200,
        disabled=True,
    )

    selector_fecha = SelectorFecha(page, on_date_selected)

    # Botón definido antes para usarlo dentro de la función
    boton_confirmar = ft.ElevatedButton(
        "Confirmar",
        icon=ft.Icons.CHECK,
        bgcolor=ft.Colors.GREEN,
    )

    # Función del click
    def confirmar_click(e):
        fecha = selector_fecha.fecha_seleccionada
        if fecha:
            guardar_encabezado_en_bd(nro_presupuesto, fecha.strftime('%d/%m/%Y'))
            print("Datos guardados en la base de datos.")
            desactivar_boton(boton_confirmar, page)
        else:
            print("No se ha seleccionado una fecha.")

    # Asignar la función después para evitar referencia circular
    boton_confirmar.on_click = confirmar_click

    return ft.Container(
        content=ft.Column([
            ft.Row(
                controls=[
                    ft.Image(
                        src="pdf_templates/assets/ol_logo.webp",
                        width=350,
                        height=300,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Container(width=30),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        controls=[
                            campo_nro,
                            selector_fecha,
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Container(height=20),
            ft.Row([boton_confirmar], alignment=ft.MainAxisAlignment.CENTER)
        ]),
        padding=20,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY, offset=ft.Offset(2, 2)),
    )
