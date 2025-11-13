# ui/consultas/reimpresion_menu.py 
import os
import flet as ft
from ui.consultas.generar_pdf_reimpresion import generar_pdf_reimpresion
from ui.utils.alerta_conclusion import mostrar_alerta
from db.db_config import get_connection

def mostrar_reimpresion(page: ft.Page):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLUE_GREY_300
    page.title = "OL Maderas - Reimprimir Presupuesto"

    conn = get_connection()

    # --- Obtener lista de presupuestos ---
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id_presupuesto, p.fecha, c.razon_social
        FROM presupuestos p
        JOIN clientes c ON p.id_cliente = c.id_cliente
        ORDER BY p.id_presupuesto DESC
    """)
    presupuestos = cursor.fetchall()  # lista de tuplas (numero, fecha, cliente)

    conn.close()

    # --- Contenedor con lista de presupuestos ---
    controles_lista = []
    for id_presupuesto, fecha, cliente in presupuestos:
        controles_lista.append(
            ft.Text(f"Nro presup.: {id_presupuesto} | Fecha: {fecha} | Cliente: {cliente}", size=18)
        )

    # Caja con scroll para mostrar hasta 5 filas visibles
    lista_presupuestos = ft.Container(
        content=ft.Column(
            controls=controles_lista,
            spacing=5,
            scroll=ft.ScrollMode.AUTO  # scroll va aquí
        ),
        height=180,
        padding=ft.padding.all(10),
        border_radius=ft.border_radius.all(12),
        bgcolor=ft.Colors.BLUE_GREY_50
    )


    # --- Input para seleccionar presupuesto ---
    input_numero = ft.TextField(label="Ingrese número de presupuesto a reimprimir", width=300)

    def reimprimir(e):
        nro = input_numero.value.strip()
        if not nro:
            mostrar_alerta(page, "Debe ingresar un número de presupuesto")
            return

        conn = get_connection()
        cursor = conn.cursor()

        # 1. Datos del presupuesto
        cursor.execute("""
            SELECT id_presupuesto, fecha, id_cliente, moneda, subtotal, descuento_porcentaje, 
                descuento_valor, iva_105, iva_21, total_final, total_letras,
                validez_oferta, forma_pago, condicion_pago, plazo_entrega, lugar_entrega, transporte
            FROM presupuestos
            WHERE id_presupuesto = ?
        """, (nro,))
        presu = cursor.fetchone()
        if not presu:
            conn.close()
            mostrar_alerta(page, f"Presupuesto {nro} no encontrado")
            return

        (id_presupuesto, fecha, id_cliente, moneda, subtotal, descuento_porcentaje, descuento_valor,
        iva_105, iva_21, total_final, total_letras, validez_oferta, forma_pago, condicion_pago,
        plazo_entrega, lugar_entrega, transporte) = presu

        # 2. Datos del cliente
        cursor.execute("""
            SELECT razon_social, cuit_dni, domicilio, provincia, localidad, telefono, email, condicion_iva
            FROM clientes WHERE id_cliente = ?
        """, (id_cliente,))
        cliente_data = cursor.fetchone()
        conn.close()

        cliente = {
            "razon_social": cliente_data[0],
            "cuit": cliente_data[1],
            "domicilio": cliente_data[2],
            "provincia": cliente_data[3],
            "localidad": cliente_data[4],
            "telefono": cliente_data[5],
            "email": cliente_data[6],
            "condicion_iva": cliente_data[7],
        }

        # 3. Ítems
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cantidad, descripcion, precio_unitario, total FROM items WHERE id_presupuesto = ?", (nro,))
        items = [{"cantidad": i[0], "descripcion": i[1], "precio_unitario": i[2], "total": i[3]} for i in cursor.fetchall()]
        conn.close()

        # 4. Armar diccionario final
        datos_pdf = {
            "numero_presupuesto": id_presupuesto,
            "fecha": fecha,
            "cliente": cliente,
            "items": items,
            "subtotal": subtotal,
            "descuento_porcentaje": descuento_porcentaje,
            "descuento_valor": descuento_valor,
            "iva_105": iva_105,
            "iva_21": iva_21,
            "total_final": total_final,
            "total_letras": total_letras,
            "moneda": moneda,
            "validez_oferta": validez_oferta,
            "forma_pago": forma_pago,
            "condicion_pago": condicion_pago,
            "plazo_entrega": plazo_entrega,
            "lugar_entrega": lugar_entrega,
            "transporte": transporte
        }

        # 5. Generar PDF usando una función nueva
        pdf_path = generar_pdf_reimpresion(datos_pdf)
        os.startfile(pdf_path)  # abre automáticamente el PDF en Windows
        mostrar_alerta(page, f"PDF del presupuesto nro: {id_presupuesto}; fue re-generado correctamente")

    # --- Botones ---
    boton_style = ft.ButtonStyle(text_style=ft.TextStyle(size=22))
    botones = ft.Row(
        [
            ft.ElevatedButton("Reimprimir", width=220, height=50, bgcolor=ft.Colors.GREEN_200, style=boton_style, on_click=reimprimir),
            ft.ElevatedButton("Volver", width=220, height=50, bgcolor=ft.Colors.RED_400, style=boton_style, on_click=lambda e: mostrar_consultas(page))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=25
    )

    # --- Layout principal ---
    page.add(
        ft.Column(
            [
                ft.Text("Lista de presupuestos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
                lista_presupuestos,
                input_numero,
                botones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )
    )
    page.update()
