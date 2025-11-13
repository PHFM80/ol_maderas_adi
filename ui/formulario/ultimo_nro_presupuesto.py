# ui/formulario/ultimo_nro_presupuesto.py
def ultimo_nro_presupuesto(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id_presupuesto) FROM presupuestos")
    resultado = cursor.fetchone()
    cursor.close()
    if resultado[0] is None:
        return 0
    return int(resultado[0])
