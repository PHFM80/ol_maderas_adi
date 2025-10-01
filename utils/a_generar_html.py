# utils/a_generar_html.py

import os
import sqlite3
from jinja2 import Environment, FileSystemLoader

def renderizar_html_desde_bd():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(base_dir, "../pdf_templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("presupuesto.html")

    db_path = os.path.join(base_dir, "../db/presupuesto.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Lectura encabezado
    cursor.execute("SELECT * FROM encabezado ORDER BY ROWID DESC LIMIT 1")
    encabezado = cursor.fetchone()
    numero_presupuesto = encabezado[0] if encabezado else "-"
    fecha = encabezado[1] if encabezado else "-"

    # Lectura cliente
    cursor.execute("SELECT * FROM datos_cliente ORDER BY ROWID DESC LIMIT 1")
    cliente = cursor.fetchone()
    cliente_dict = {
        "razon_social": cliente[0] if cliente else "",
        "domicilio": cliente[1] if cliente else "",
        "provincia": cliente[2] if cliente else "",
        "localidad": cliente[3] if cliente else "",
        "cuit": cliente[4] if cliente else "",
        "condicion_iva": cliente[5] if cliente else "",
        "telefono": cliente[6] if cliente else "",
        "email": cliente[7] if cliente else "",
    }

    # Lectura items
    cursor.execute("SELECT cantidad, descripcion, precio_unitario, total FROM detalle_producto")
    items = [dict(cantidad=row[0], descripcion=row[1], precio_unitario=row[2], total=row[3]) for row in cursor.fetchall()]

    # Cálculo subtotal (suma de totales en items)
    subtotal = sum(item["total"] for item in items)

    # Lectura últimos valores del presupuesto (descuento, iva, total, letras)
    cursor.execute("SELECT subtotal, descuento_porcentaje, descuento_valor, iva_105, iva_21, total_final, total_letras FROM valores_presupuesto ORDER BY id DESC LIMIT 1")
    valores = cursor.fetchone()
    if valores:
        subtotal = valores[0]
        descuento = {"porcentaje": valores[1], "valor": valores[2]}
        iva_105 = valores[3]
        iva_21 = valores[4]
        total_final = valores[5]
        total_letras = valores[6]
    else:
        # Valores por defecto si no hay registro
        descuento = {"porcentaje": 0, "valor": 0}
        iva_105 = 0
        iva_21 = 0
        total_final = subtotal
        total_letras = ""

    # Moneda
    cursor.execute("SELECT moneda FROM moneda ORDER BY ROWID DESC LIMIT 1")
    moneda_row = cursor.fetchone()
    moneda = moneda_row[0] if moneda_row else "Pesos"

    # Condiciones de venta
    cursor.execute("SELECT * FROM condiciones_venta ORDER BY ROWID DESC LIMIT 1")
    condiciones = cursor.fetchone()
    condiciones_dict = {
        "validez": condiciones[0] if condiciones else "",
        "forma_pago": condiciones[1] if condiciones else "",
        "condiciones_pago": condiciones[2] if condiciones else "",
        "plazo_entrega": condiciones[3] if condiciones else "",
        "lugar_entrega": condiciones[4] if condiciones else "",
        "transporte": condiciones[5] if condiciones else "",
    }

    conn.close()

    # Renderizar plantilla con los datos
    html_renderizado = template.render(
        numero_presupuesto=numero_presupuesto,
        fecha=fecha,
        cliente=cliente_dict,
        items=items,
        subtotal=subtotal,
        descuento=descuento,
        iva_105=iva_105,
        iva_21=iva_21,
        total_final=total_final,
        total_letras=total_letras,
        moneda=moneda,
        validez=condiciones_dict["validez"],
        forma_pago=condiciones_dict["forma_pago"],
        condiciones_pago=condiciones_dict["condiciones_pago"],
        plazo_entrega=condiciones_dict["plazo_entrega"],
        lugar_entrega=condiciones_dict["lugar_entrega"],
        transporte=condiciones_dict["transporte"],
    )

    return html_renderizado
