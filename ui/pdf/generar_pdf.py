# ui/pdf/generar_pdf.py

from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime
from pathlib import Path
from weasyprint import HTML
from .buscar_x_id import obtener_cliente_por_id

def generar_pdf(datos_presupuesto, items, resumen, condiciones):

    # --- Obtener cliente completo ---
    id_cliente = datos_presupuesto.get("id_cliente")
    cliente_completo = obtener_cliente_por_id(id_cliente)

    # 1️⃣ Configurar Jinja2 y cargar plantilla
    plantilla_dir = os.path.join(os.path.dirname(__file__), "..", "..", "pdf_templates")
    env = Environment(loader=FileSystemLoader(plantilla_dir))
    template = env.get_template("presupuesto.html")

    # 2️⃣ Preparar el contexto para renderizar la plantilla
    context = {
        "numero_presupuesto": datos_presupuesto.get("numero_presupuesto", "—"),
        "fecha": datos_presupuesto.get("fecha", datetime.today().strftime("%d/%m/%Y")),
        "cliente": cliente_completo,
        "items": items,
        "subtotal": resumen.get("subtotal", 0),
        "descuento_porcentaje": resumen.get("descuento_porcentaje", 0),
        "descuento_valor": resumen.get("descuento_valor", 0),
        "iva_105": resumen.get("iva_105", 0),
        "iva_21": resumen.get("iva_21", 0),
        "total_final": resumen.get("total", 0),
        "total_letras": resumen.get("total_letras", ""),
        "moneda": resumen.get("moneda", "ARS"),
        "validez_oferta": condiciones.get("validez_oferta", ""),
        "plazo_entrega": condiciones.get("plazo_entrega", ""),
        "lugar_entrega": condiciones.get("lugar_entrega", ""),
        "transporte": condiciones.get("transporte", ""),
        "forma_pago": condiciones.get("forma_pago", ""),
        "condicion_pago": condiciones.get("condicion_pago", "")
    }

    # 3️⃣ Renderizar HTML con Jinja2
    html_renderizado = template.render(context)

    # 4️⃣ Definir ruta de salida del PDF en Descargas
    nombre_archivo = f"OL_maderas-presupuesto_nro_{datos_presupuesto.get('numero_presupuesto', 'generico')}.pdf"
    carpeta_descargas = str(Path.home() / "Downloads")
    if not os.path.exists(carpeta_descargas):
        os.makedirs(carpeta_descargas)
    pdf_path = os.path.join(carpeta_descargas, nombre_archivo)

    # 5️⃣ Generar PDF con WeasyPrint, asegurando base_url para CSS e imágenes
    HTML(string=html_renderizado, base_url=plantilla_dir).write_pdf(pdf_path)

    # 6️⃣ Abrir el PDF automáticamente
    try:
        os.startfile(pdf_path)  # Windows
    except AttributeError:
        import subprocess
        subprocess.run(["open" if os.name == "posix" else "xdg-open", pdf_path])

    print(f"PDF generado correctamente en: {pdf_path}")
    return pdf_path
