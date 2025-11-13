# ui/previsualizacion/previsualizacion_ui.py
import flet as ft
from .datos_presupuesto_ui import crear_contenedor_datos
from .tabla_items_ui import crear_tabla_items
from .resumen_ui import crear_resumen
from .condiciones_ui import crear_condiciones
from ui.pdf.guardar_presupuesto import guardar_presupuesto
from ui.pdf.generar_pdf import generar_pdf
from ..utils.alerta_conclusion import mostrar_alerta



def mostrar_previsualizacion(page: ft.Page, datos_presupuesto, items, resumen, condiciones):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "OL Maderas - Previsualización"

    # --- Título principal ---
    titulo = ft.Container(
        content=ft.Text(
            "Previsualización de Presupuesto",
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

    # --- Crear contenedores de cada sección ---
    contenedor_datos = crear_contenedor_datos(datos_presupuesto)
    contenedor_items = crear_tabla_items(items)
    contenedor_resumen, resumen_calculado = crear_resumen(resumen, items)
    contenedor_condiciones = crear_condiciones(condiciones)

    def on_generar_pdf(e):
        id_presupuesto = guardar_presupuesto(datos_presupuesto, items, resumen_calculado, condiciones)
        if id_presupuesto:
            generar_pdf(datos_presupuesto, items, resumen_calculado, condiciones)
            mostrar_alerta(page, f"Presupuesto guardado y PDF generado.")
        else:
            mostrar_alerta(page, "Error al guardar el presupuesto")

    # --- Botones inferiores (por ahora sin funcionalidad) ---
    def volver_menu(e):
        from menu import menu_principal
        menu_principal(page)
    
    boton_style = ft.ButtonStyle(text_style=ft.TextStyle(size=22))
    from ui.formulario import formulario
    botones = ft.Row(
        [
            ft.ElevatedButton(
                "Generar PDF",
                width=220,
                height=50,
                bgcolor=ft.Colors.GREEN_200,
                style=boton_style,
                on_click=on_generar_pdf
            ),
            ft.ElevatedButton(
                "Modificar Datos",
                width=220,
                height=50,
                bgcolor=ft.Colors.ORANGE_200,
                style=boton_style,
                on_click=lambda e: formulario.mostrar_formulario(
                    page,
                    datos_presupuesto=datos_presupuesto,
                    items=items,
                    resumen=resumen,
                    condiciones=condiciones
                )
            ),
            ft.ElevatedButton("Volver al Menú", on_click=volver_menu, width=220, height=50, bgcolor=ft.Colors.RED_400, style=boton_style),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=25
    )

    # --- Layout principal ---
    page.add(
        ft.Column(
            [
                titulo,
                contenedor_datos,
                contenedor_items,
                contenedor_resumen,
                contenedor_condiciones,
                botones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            scroll=ft.ScrollMode.AUTO
        )
    )
    page.update()
