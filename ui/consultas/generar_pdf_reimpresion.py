# ui/consultas/generar_pdf_reimpresion.py

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os
from pathlib import Path

def generar_pdf_reimpresion(datos_pdf):
    """
    Genera un PDF de un presupuesto usando los datos recibidos.
    No busca nada en la BD, no guarda nada. Solo arma el PDF con el formato.
    """
    # Carpeta de plantillas
    plantilla_dir = os.path.join(os.path.dirname(__file__), "..", "..", "pdf_templates")
    env = Environment(loader=FileSystemLoader(plantilla_dir))
    template = env.get_template("presupuesto.html")

    # Renderizar HTML con los datos recibidos
    html_renderizado = template.render(datos_pdf)

    # Definir ruta de salida en Descargas
    nombre_archivo = f"OL_maderas-presupuesto_nro_{datos_pdf.get('numero_presupuesto', 'generico')}.pdf"
    carpeta_descargas = str(Path.home() / "Downloads")
    if not os.path.exists(carpeta_descargas):
        os.makedirs(carpeta_descargas)
    pdf_path = os.path.join(carpeta_descargas, nombre_archivo)

    # Generar PDF con WeasyPrint
    HTML(string=html_renderizado, base_url=plantilla_dir).write_pdf(pdf_path)

    # Abrir automáticamente el PDF (Windows)
    try:
        os.startfile(pdf_path)
    except AttributeError:
        import subprocess
        subprocess.run(["open" if os.name == "posix" else "xdg-open", pdf_path])

    print(f"PDF generado correctamente en: {pdf_path}")
    return pdf_path
