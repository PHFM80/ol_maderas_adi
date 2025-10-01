# ui/formulario.py

import flet as ft
from ui.componentes.encabezado.encabezado_presupuesto import EncabezadoPresupuesto
from ui.componentes.datos_clientes.datos_clientes import vista_datos_clientes
from ui.componentes.elementos_tabla.elementos_tabla import ElementosTabla
from ui.componentes.calculo_valor_total.calculo_valor_total import calculo_valor_total
from ui.componentes.condiciones.condiciones import condiciones_venta
from ui.componentes.generar_pdf.generar_pdf import generar_pdf


def formulario(page, on_date_selected):

    elementos_tabla = ElementosTabla(page)  # crear instancia
    return ft.Column(
        controls=[
            # 1) Encabezado del presupuesto
            EncabezadoPresupuesto(page, on_date_selected),

            # 2) Datos del cliente
            vista_datos_clientes(page),

            # 3) Detalle de items (moneda, formulario y tabla)
            elementos_tabla.get_container(),  

            # 4) Condiciones de venta
            calculo_valor_total(page),

            # 5) Condiciones de venta
            condiciones_venta(page),

            # 6) boton de descargar
            generar_pdf(page),

        ],
        spacing=20,          # espacio vertical entre secciones
        scroll="auto",       # si el contenido se extiende, permite scroll
        expand=True          # ocupa todo el alto disponible
    )
