# utils\pdf_generator.py

import flet as ft
from utils.a_generar_html import renderizar_html_desde_bd
from utils.b_generar_pdf_desde_html import generar_pdf_desde_html
from utils.c_actualizar_nro_presupuesto import actualizar_nro_presupuesto
from utils.d_eliminar_bd import eliminar_base_de_datos
from utils.e_abrir_pdf import abrir_pdf
from utils.f_cerrar_app import cerrar_app

def pdf_generator(page):
    # a) Renderizar HTML con datos desde BD
    html_renderizado = renderizar_html_desde_bd()

    # b) Generar PDF a partir del HTML renderizado
    ruta_pdf = generar_pdf_desde_html(html_renderizado)

    # c) Actualizar número de presupuesto (archivo txt)
    actualizar_nro_presupuesto()

    # d) Eliminar base de datos para limpiar
    eliminar_base_de_datos()

    # e) Abrir el PDF generado en el sistema
    abrir_pdf(ruta_pdf)

    # f) Mostrar notificación y cerrar o refrescar app
    cerrar_app(page)

