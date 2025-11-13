def limpiar_campos(campos, page):
    """
    Limpia todos los campos y actualiza la página.
    """
    for campo in campos:
        if hasattr(campo, "options"):  # Dropdown
            campo.value = None
        else:  # TextField
            campo.value = ""
    page.update()
