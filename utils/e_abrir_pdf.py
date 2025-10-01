# utils\e_abrir_pdf.py
import os
import platform
import subprocess

def abrir_pdf(ruta_pdf):
    sistema = platform.system()
    if sistema == "Windows":
        os.startfile(ruta_pdf)
    elif sistema == "Darwin":  # macOS
        subprocess.call(["open", ruta_pdf])
    else:  # Linux y otros
        subprocess.call(["xdg-open", ruta_pdf])
