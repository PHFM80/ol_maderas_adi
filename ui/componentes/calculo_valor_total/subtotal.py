# ui/componentes/calculo_valor_total/subtotal.py

import flet as ft
import sqlite3
import os

def componente_subtotal(subtotal, page, refrescar_callback):
    label = ft.Text("Subtotal:", size=16, weight=ft.FontWeight.BOLD, width=150 )
    boton_calcular = ft.ElevatedButton( "Calcular", on_click=lambda e: refrescar_callback(valor, page))
    valor = ft.TextField(
    value=f"$ {subtotal:.2f}",
    read_only=True,
    text_align=ft.TextAlign.RIGHT,
    width=260,
    border=ft.InputBorder.NONE,
    filled=False
)


    fila = ft.Row(
        controls=[label, boton_calcular, valor],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=500
    )

    return fila, valor


def refrescar_subtotal(control_subtotal, page):
    # 1) Calcular subtotal desde BD
    ruta_db = os.path.join(os.path.dirname(__file__), "../../../db/presupuesto.db")
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT total FROM detalle_producto")
    filas = cursor.fetchall()
    conexion.close()

    subtotal = sum(fila[0] for fila in filas if fila[0] is not None)
    print(f"✅ SUBTOTAL ACTUALIZADO: {subtotal}")

    # 2) Actualizar el control con el nuevo subtotal
    control_subtotal.value = f"$ {subtotal:.2f}"

#    control_subtotal.text = f"$ {subtotal:.2f}"
    control_subtotal.update()

    # 3) Refrescar la UI
    page.update()
