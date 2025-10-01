# ui\componentes\encabezado\nuevo_nro_presup.py
import os

def obtener_nuevo_numero():
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    archivo = os.path.join(raiz_proyecto, "presupuesto_anterior.txt")
    print("Leyendo archivo en:", archivo)

    try:
        with open(archivo, "r") as f:
            nro = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        nro = 0
    return nro + 1

