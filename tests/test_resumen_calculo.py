from ui.previsualizacion.resumen_ui import crear_resumen

def test_calculo_resumen():
    items = [
        {"descripcion": "Tabla pino", "cantidad": 2, "precio_unitario": 1500, "total": 3000},
        {"descripcion": "Clavos", "cantidad": 1, "precio_unitario": 500, "total": 500},
    ]
    resumen = {"descuento": 10, "iva_105": False, "iva_21": True}

    _, resumen_calculado = crear_resumen(resumen, items)

    assert resumen_calculado["subtotal"] == 3500
    assert resumen_calculado["descuento_valor"] == 350
    assert resumen_calculado["subtotal_con_descuento"] == 3150
    assert resumen_calculado["iva_21"] == round(3150 * 0.21, 2)
    assert resumen_calculado["total"] == round(3150 * 1.21, 2)
