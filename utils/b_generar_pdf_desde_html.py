# utils/b_generar_pdf_desde_html.py

import os, sqlite3
from pathlib import Path
from weasyprint import HTML


def generar_pdf_desde_html(html_renderizado):
    def obtener_nro_presupuesto():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "../db/presupuesto.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT nro_presupuesto FROM encabezado ORDER BY ROWID DESC LIMIT 1")
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] if resultado else None
    nro = obtener_nro_presupuesto()

    downloads_path = str(Path.home() / "Downloads")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_templates_dir = os.path.join(base_dir, "../pdf_templates")

    if not os.path.exists(downloads_path):
        os.makedirs(downloads_path)

    nombre_pdf = f"OL_maderas-presupuesto_nro_{nro}.pdf" if nro else "presupuesto_generado.pdf"
    pdf_path = os.path.join(downloads_path, nombre_pdf)

    HTML(string=html_renderizado, base_url=pdf_templates_dir).write_pdf(pdf_path)

    return pdf_path
