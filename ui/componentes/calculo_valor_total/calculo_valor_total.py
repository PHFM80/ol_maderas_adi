# ui\componentes\calculo_valor_total\calculo_valor_total.py

import flet as ft
from ui.componentes.calculo_valor_total.subtotal import componente_subtotal, refrescar_subtotal
from ui.componentes.calculo_valor_total.descuento import componente_descuento, calcular_descuento
from ui.componentes.calculo_valor_total.iva import componente_iva
from ui.componentes.calculo_valor_total.total import componente_total 
from ui.componentes.calculo_valor_total.guardar_valores_presupuesto import guardar_valores_presupuesto
from ui.componentes.funciones.desactivar_boton import desactivar_boton


def calculo_valor_total(page):
    titulo = ft.Text("CÁLCULO VALOR TOTAL", size=20, weight=ft.FontWeight.BOLD)

    # 1) Subtotal
    fila_subtotal, control_subtotal = componente_subtotal(0, page, refrescar_subtotal)


    # 2) Descuento
    fila_descuento, resultado_descuento, campo_porcentaje = componente_descuento(control_subtotal)

    # 3) IVA (usando el resultado del descuento como valor base)
    fila_iva, resultado_iva_105, resultado_iva_21 = componente_iva(resultado_descuento)

    # 4) Total (usando valores ya expuestos)
    fila_total, resultado_total, resultado_total_letras = componente_total(
        resultado_descuento,
        resultado_iva_105,
        resultado_iva_21
    )

    cuerpo_calculo = ft.Column([
        fila_subtotal,
        fila_descuento, 
        fila_iva,
        fila_total,
        
    ], spacing=10)

    def confirmar_click(e):
        guardar_valores_presupuesto(
            control_subtotal,
            campo_porcentaje,
            resultado_descuento,
            resultado_iva_105,
            resultado_iva_21,
            resultado_total,
            resultado_total_letras
        )
        desactivar_boton(e.control, page)


    boton_confirmar = ft.ElevatedButton(
        "Confirmar",
        icon=ft.Icons.CHECK,
        bgcolor=ft.Colors.GREEN,
        on_click=confirmar_click
    )

    return ft.Container(
        content=ft.Column([
            titulo,
            ft.Divider(),
            cuerpo_calculo,
            ft.Container(height=20),
            ft.Row([boton_confirmar], alignment=ft.MainAxisAlignment.CENTER)
        ]),
        padding=20,
        border=ft.border.all(1, ft.Colors.GREY),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY, offset=ft.Offset(2, 2)),
    )
