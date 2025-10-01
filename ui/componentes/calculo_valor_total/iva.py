# ui\componentes\calculo_valor_total\iva.py

import flet as ft

def componente_iva(valor_base):
    resultado_iva_105 = ft.Text("$ 0.00", size=16, text_align=ft.TextAlign.RIGHT, width=250)
    resultado_iva_21 = ft.Text("$ 0.00", size=16, text_align=ft.TextAlign.RIGHT, width=250)

    chk_iva_105 = ft.Checkbox(label="", value=False)
    chk_iva_21 = ft.Checkbox(label="", value=False)

    def on_check_change(e):
        # Desmarcar la otra opción si una es seleccionada
        if e.control == chk_iva_105 and chk_iva_105.value:
            chk_iva_21.value = False
        elif e.control == chk_iva_21 and chk_iva_21.value:
            chk_iva_105.value = False

        # Reiniciar valores
        resultado_iva_105.value = "$ 0.00"
        resultado_iva_21.value = "$ 0.00"

        # Calcular IVA
        base = float(valor_base.value.replace("$", "").replace(" ", ""))
        if chk_iva_105.value:
            porcentaje = 10.5
            monto_iva = base * (porcentaje / 100)
            resultado_iva_105.value = f"$ {monto_iva:.2f}"
        elif chk_iva_21.value:
            porcentaje = 21.0
            monto_iva = base * (porcentaje / 100)
            resultado_iva_21.value = f"$ {monto_iva:.2f}"

        e.control.page.update()

    chk_iva_105.on_change = on_check_change
    chk_iva_21.on_change = on_check_change

    fila_105 = ft.Row([
        ft.Text("IVA 10.5% :", size=16, width=100, weight=ft.FontWeight.BOLD),
        chk_iva_105,
        resultado_iva_105
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=500)

    fila_21 = ft.Row([
        ft.Text("IVA 21% :", size=16, width=100, weight=ft.FontWeight.BOLD),
        chk_iva_21,
        resultado_iva_21
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, width=500)

    return ft.Column([fila_105, fila_21], spacing=10), resultado_iva_105, resultado_iva_21
