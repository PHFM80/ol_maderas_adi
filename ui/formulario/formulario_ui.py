# ui/formulario/formulario_ui.py
import flet as ft

from .selector_fecha import SelectorFecha
from .items_ui import crear_campos_items


CONTENEDOR_WIDTH = 800
CONTROL_INTERNO_WIDTH = 600

# -------------------- SECCIÓN 1: CLIENTE --------------------
def crear_campos_cliente(clientes_options):
    cliente_dropdown = ft.Dropdown(
        label="Seleccionar Cliente",
        width=CONTROL_INTERNO_WIDTH,
        options=clientes_options,
        menu_height=300  # ← scroll automático (6 ítems aprox)
    )
    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text("Cliente", size=22, weight=ft.FontWeight.BOLD),
                cliente_dropdown
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        width=CONTENEDOR_WIDTH,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor, cliente_dropdown

# -------------------- SECCIÓN 2: DATOS DEL PRESUPUESTO --------------------
def crear_campos_datos(page: ft.Page, on_date_selected, numero_presupuesto_valor):
    numero_presupuesto = ft.TextField(
        width=150,
        disabled=True,
        value=numero_presupuesto_valor
    )
    texto_num_presupuesto = ft.Row(
        [
            ft.Text("El número de presupuesto es:", size=18, weight=ft.FontWeight.W_600),
            numero_presupuesto
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    selector_fecha = SelectorFecha(page, on_date_selected)
    moneda = ft.Dropdown(
        label="Moneda",
        width=CONTROL_INTERNO_WIDTH,
        options=[ft.dropdown.Option("ARS"), ft.dropdown.Option("USD")]
    )
    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text("Datos del Presupuesto", size=22, weight=ft.FontWeight.BOLD),
                texto_num_presupuesto,
                selector_fecha,
                moneda
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        width=CONTENEDOR_WIDTH,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor, numero_presupuesto, selector_fecha, moneda

# -------------------- SECCIÓN 3: INGRESO DE ÍTEMS --------------------

# Solo importamos la función; la llamaremos desde mostrar_formulario
# items_contenedor, boton_items, items_list, total_general_text = crear_campos_items()

# -------------------- SECCIÓN 4: RESUMEN IMPOSITIVO --------------------
def crear_campos_resumen():
    descuento = ft.TextField(label="Descuento (%)", width=150, on_focus=lambda e: setattr(e.control, "value", "") )
    iva_105 = ft.Checkbox(label="IVA 10.5%", value=False)
    iva_21 = ft.Checkbox(label="IVA 21%", value=True)

    def cambiar_iva(e, otro):
        if e.control.value:
            otro.value = False
            otro.update()

    iva_105.on_change = lambda e: cambiar_iva(e, iva_21)
    iva_21.on_change = lambda e: cambiar_iva(e, iva_105)

    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text("Resumen Impositivo", size=22, weight=ft.FontWeight.BOLD),
                ft.Row([descuento], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([iva_105, iva_21], alignment=ft.MainAxisAlignment.CENTER, spacing=40)
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        width=CONTENEDOR_WIDTH,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor, descuento, iva_105, iva_21

# -------------------- SECCIÓN 5: CONDICIONES COMERCIALES --------------------
def crear_campos_condiciones():
    validez_oferta = ft.TextField(label="Validez de la oferta", width=CONTROL_INTERNO_WIDTH)
    forma_pago = ft.TextField(label="Forma de pago", width=CONTROL_INTERNO_WIDTH)
    condicion_pago = ft.TextField(label="Condición de pago", width=CONTROL_INTERNO_WIDTH)
    plazo_entrega = ft.TextField(label="Plazo de entrega", width=CONTROL_INTERNO_WIDTH)
    lugar_entrega = ft.TextField(label="Lugar de entrega", width=CONTROL_INTERNO_WIDTH)
    transporte = ft.TextField(label="Transporte", width=CONTROL_INTERNO_WIDTH)
    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text("Condiciones Comerciales", size=22, weight=ft.FontWeight.BOLD),
                validez_oferta,
                forma_pago,
                condicion_pago,
                plazo_entrega,
                lugar_entrega,
                transporte
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        width=CONTENEDOR_WIDTH,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )
    return contenedor, validez_oferta, forma_pago, condicion_pago, plazo_entrega, lugar_entrega, transporte
