import flet as ft
from num2words import num2words

def numero_a_letras(numero):
    entero = int(numero)
    decimal = round((numero - entero) * 100)

    letras_entero = num2words(entero, lang='es').capitalize()
    if decimal > 0:
        letras_decimal = num2words(decimal, lang='es')
        return f"{letras_entero} con {letras_decimal} centavos"
    else:
        return letras_entero

def componente_total(valor_descuento_control, iva_105_control, iva_21_control):
    resultado_total = ft.Text("$ 0.00", size=16, text_align=ft.TextAlign.RIGHT, width=350)
    resultado_total_letras = ft.Text("Son: cero", size=16, italic=True)

    def calcular_total(e):
        try:
            descuento = float(valor_descuento_control.value.replace("$", "").strip())
            iva_105 = float(iva_105_control.value.replace("$", "").strip())
            iva_21 = float(iva_21_control.value.replace("$", "").strip())

            total = descuento + iva_105 + iva_21
            resultado_total.value = f"$ {total:.2f}"
            resultado_total_letras.value = f"Son: {numero_a_letras(total)}"
        except Exception:
            resultado_total.value = "Error en el cálculo"
            resultado_total_letras.value = ""

        e.control.page.update()

    boton_calcular = ft.ElevatedButton("Calcular Total", on_click=calcular_total)

    fila_total = ft.Column([
        boton_calcular,
        ft.Row([
            ft.Text("Total:", size=16, weight=ft.FontWeight.BOLD),
            resultado_total
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=500),
        resultado_total_letras,
    ])

    return fila_total, resultado_total, resultado_total_letras
