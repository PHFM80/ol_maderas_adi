# ui/componentes/calculo_valor_total/descuento.py

import flet as ft

def calcular_descuento(subtotal, porcentaje):
    if porcentaje < 0 or porcentaje > 100:
        return None
    return subtotal - (subtotal * (porcentaje / 100))


def componente_descuento(control_subtotal):
    descuento_input = ft.TextField(
        label="(%)",
        width=50,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    resultado_descuento = ft.Text(
        "$ 0.00",
        size=16, text_align=ft.TextAlign.RIGHT, width=140
    )

    def aplicar_descuento(e):
        try:
            subtotal_texto = control_subtotal.value.replace("$", "").strip()
            subtotal = float(subtotal_texto)

            porcentaje = float(descuento_input.value)
            if porcentaje < 0 or porcentaje > 100:
                resultado_descuento.value = "Valor inválido"
            else:
                monto_descuento = subtotal * (porcentaje / 100)
                total_con_descuento = subtotal - monto_descuento
                resultado_descuento.value = f"$ {total_con_descuento:.2f}"
        except ValueError:
            resultado_descuento.value = "Error"

        e.control.page.update()

    boton_aplicar = ft.ElevatedButton(
        "Aplicar descuento",
        on_click=aplicar_descuento
    )

    fila = ft.Row(
        controls=[
            ft.Text("Descuento:", size=16, weight=ft.FontWeight.BOLD),
            descuento_input,
            ft.Text("%"),
            boton_aplicar,
            ft.Container(width=30),
            resultado_descuento,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        wrap=True,
    )

    return fila, resultado_descuento, descuento_input

