import flet as ft

def crear_condiciones(condiciones):
    condiciones_column = ft.Column(
        [
            ft.Text("Condiciones Comerciales:", size=20, weight=ft.FontWeight.BOLD),
            ft.Text(f"Validez oferta: {condiciones['validez_oferta']}"),
            ft.Text(f"Forma de pago: {condiciones['forma_pago']}"),
            ft.Text(f"Condición de pago: {condiciones['condicion_pago']}"),
            ft.Text(f"Plazo de entrega: {condiciones['plazo_entrega']}"),
            ft.Text(f"Lugar de entrega: {condiciones['lugar_entrega']}"),
            ft.Text(f"Transporte: {condiciones['transporte']}"),
        ],
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

    contenedor = ft.Container(
        content=condiciones_column,
        padding=20,
        width=800,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor
