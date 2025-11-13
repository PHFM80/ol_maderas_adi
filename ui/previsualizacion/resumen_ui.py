# ui/previsualizacion/resumen_ui.py
import flet as ft
import locale
from num2words import num2words  # para convertir total a letras

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')  # para formato argentino

def formatear_moneda(valor):
    return "$ " + locale.format_string("%.2f", valor, grouping=True).replace(".", "X").replace(",", ".").replace("X", ",")

def crear_resumen(resumen, items):
    # --- Cálculos ---
    subtotal = round(sum(item["total"] for item in items), 2)
    descuento_raw = resumen.get("descuento", 0)

    # Validación robusta
    try:
        descuento_float = float(descuento_raw)
        # Rango permitido 1–100
        if not (1 <= descuento_float <= 100):
            descuento_float = 0.0
    except (ValueError, TypeError):
        # Si llega letra, cadena vacía u otro valor no numérico → 0
        descuento_float = 0.0
    descuento_valor = round(subtotal * (descuento_float / 100), 2)
    subtotal_con_descuento = round(subtotal - descuento_valor, 2)
    iva_105_valor = round(subtotal_con_descuento * 0.105, 2) if resumen.get("iva_105") else 0
    iva_21_valor = round(subtotal_con_descuento * 0.21, 2) if resumen.get("iva_21") else 0
    total = round(subtotal_con_descuento + iva_105_valor + iva_21_valor, 2)

    # --- Convertir total a letras ---
    entero = int(total)
    decimal = int(round((total - entero) * 100))  # dos decimales exactos
    if decimal > 0:
        total_letras = f"{num2words(entero, lang='es')} con {num2words(decimal, lang='es')}"
    else:
        total_letras = num2words(entero, lang='es')
    total_letras = total_letras.capitalize()
    
    # --- Contenedor UI ---
    resumen_column = ft.Column(
        [
            ft.Text("Resumen Impositivo:", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"Subtotal: {formatear_moneda(subtotal)}"),
            ft.Text(f"Descuento ({resumen.get('descuento',0)}%): -{formatear_moneda(descuento_valor)}"),
            ft.Text(f"Subtotal con descuento: {formatear_moneda(subtotal_con_descuento)}"),
            ft.Text(f"IVA 10.5%: {formatear_moneda(iva_105_valor)}"),
            ft.Text(f"IVA 21%: {formatear_moneda(iva_21_valor)}"),
            ft.Text(f"Total: {formatear_moneda(total)}", weight=ft.FontWeight.BOLD),
            ft.Text(f"Importe en letras : {total_letras}", weight=ft.FontWeight.BOLD),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

    contenedor = ft.Container(
        content=resumen_column,
        padding=20,
        width=800,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )

    # --- Diccionario con los datos calculados para guardar ---
    resumen_calculado = {
        "subtotal": subtotal,
        "descuento_porcentaje": descuento_float,
        "descuento_valor": descuento_valor,
        "subtotal_con_descuento": subtotal_con_descuento,
        "iva_105": iva_105_valor,
        "iva_21": iva_21_valor,
        "total": total,
        "total_letras": total_letras
    }

    return contenedor, resumen_calculado
