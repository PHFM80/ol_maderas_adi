# ui/formulario/formulario.py
import flet as ft
from .formulario_ui import (crear_campos_cliente, crear_campos_datos, crear_campos_items, crear_campos_resumen, crear_campos_condiciones)
from db.db_config import get_connection
from .selector_cliente import selector_cliente
from .ultimo_nro_presupuesto import ultimo_nro_presupuesto
from ui.previsualizacion import previsualizacion_ui as previ



def mostrar_formulario(page: ft.Page, datos_presupuesto=None, items=None, resumen=None, condiciones=None):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "OL Maderas - Generar Presupuesto"

    # --- Crear conexión a la BD ---
    conn = get_connection()  # sqlite3.Connection

    # --- Callback para selector de fecha ---
    def on_date_selected(date):
        print("Fecha seleccionada:", date)

    # --- Crear secciones ---
    clientes_options = selector_cliente(conn)
    cliente_contenedor, cliente_dropdown = crear_campos_cliente(clientes_options)

    ultimo = ultimo_nro_presupuesto(conn)
    nuevo_numero = f"{ultimo + 1:04d}" if not datos_presupuesto else datos_presupuesto["numero_presupuesto"]
    datos_contenedor, numero_presupuesto, selector_fecha, moneda = crear_campos_datos(page, on_date_selected, nuevo_numero)

    items_contenedor, boton_items, items_list, total_general_text = crear_campos_items()
    resumen_contenedor, descuento, iva_105, iva_21 = crear_campos_resumen()
    condiciones_contenedor, validez_oferta, forma_pago, condicion_pago, plazo_entrega, lugar_entrega, transporte = crear_campos_condiciones()

    # --- Si recibimos datos, rellenamos los campos ---
    if datos_presupuesto:
        cliente_dropdown.value = datos_presupuesto["id_cliente"]
        numero_presupuesto.value = datos_presupuesto["numero_presupuesto"]
        moneda.value = datos_presupuesto.get("moneda", "ARS")
        if selector_fecha and datos_presupuesto.get("fecha"):
            selector_fecha.fecha_seleccionada = datos_presupuesto["fecha"]
            selector_fecha.selected_date.value = f"Fecha seleccionada: {datos_presupuesto['fecha'].strftime('%d/%m/%Y')}"
    
    if items:
        items_list.clear()
        for it in items:
            items_list.append(it)

    if resumen:
        descuento.value = resumen.get("descuento", 0)
        iva_105.value = resumen.get("iva_105", False)
        iva_21.value = resumen.get("iva_21", False)

    if condiciones:
        validez_oferta.value = condiciones.get("validez_oferta", "")
        forma_pago.value = condiciones.get("forma_pago", "")
        condicion_pago.value = condiciones.get("condicion_pago", "")
        plazo_entrega.value = condiciones.get("plazo_entrega", "")
        lugar_entrega.value = condiciones.get("lugar_entrega", "")
        transporte.value = condiciones.get("transporte", "")

    # --- Funciones de navegación ---
    def volver_menu(e):
        conn.close()
        from menu import menu_principal
        menu_principal(page)

    def previsualizar(e):
        datos = {
            "numero_presupuesto": numero_presupuesto.value,
            "fecha": selector_fecha.fecha_seleccionada,
            "id_cliente": cliente_dropdown.value,
            "moneda": moneda.value,
        }
        previ.mostrar_previsualizacion(page, datos, items_list, {"descuento": descuento.value, "iva_105": iva_105.value, "iva_21": iva_21.value}, {
            "validez_oferta": validez_oferta.value,
            "forma_pago": forma_pago.value,
            "condicion_pago": condicion_pago.value,
            "plazo_entrega": plazo_entrega.value,
            "lugar_entrega": lugar_entrega.value,
            "transporte": transporte.value
        })

    # --- Botones inferiores ---
    boton_style = ft.ButtonStyle(text_style=ft.TextStyle(size=22))
    botones = ft.Row(
        [
            ft.ElevatedButton("Previsualizar datos", on_click=previsualizar, width=220, height=50, bgcolor=ft.Colors.GREEN_200, style=boton_style),
            ft.ElevatedButton("Volver al Menú", on_click=volver_menu, width=220, height=50, bgcolor=ft.Colors.RED_400, style=boton_style),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=25
    )

    # --- Layout principal ---
    titulo = ft.Container(
        content=ft.Text(
            "Generar Presupuesto",
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_GREY_900
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.symmetric(vertical=25, horizontal=30),
        bgcolor=ft.Colors.BLUE_100,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK26, blur_radius=8, offset=ft.Offset(3,3)),
    )

    contenido = ft.Column(
        [
            titulo,
            cliente_contenedor,
            datos_contenedor,
            items_contenedor,
            resumen_contenedor,
            condiciones_contenedor,
            botones
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25,
        scroll=ft.ScrollMode.AUTO
    )

    page.add(contenido)
    page.update()
