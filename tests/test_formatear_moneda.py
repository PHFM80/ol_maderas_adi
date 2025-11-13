from ui.previsualizacion.resumen_ui import formatear_moneda

def test_formatear_moneda():
    resultado = formatear_moneda(12345.5)
    assert resultado.startswith("$ ")
    assert "," in resultado  # formato ARS

