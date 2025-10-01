# utils\c_actualizar_nro_presupuesto.py
import os

def actualizar_nro_presupuesto():
    # Obtiene la ruta raíz del proyecto (sube dos niveles desde utils/)
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    archivo = os.path.join(raiz_proyecto, "presupuesto_anterior.txt")

    # Crear el archivo si no existe y leer el número
    try:
        with open(archivo, "r") as f:
            nro = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        nro = 0

    nro += 1

    # Guardar el nuevo número
    with open(archivo, "w") as f:
        f.write(str(nro))

    return nro
