# ui/formulario/items_ui.py
import flet as ft
import locale


locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')  # Formato monetario argentino

def formatear_moneda(valor):
    return "$ " + locale.format_string("%.2f", valor, grouping=True).replace(".", "X").replace(",", ".").replace("X", ",")

def crear_campos_items():
    items_list = []

    descripcion = ft.TextField(label="Descripción", width=200)
    cantidad = ft.TextField(label="Cantidad", width=80)
    precio_unitario = ft.TextField(label="Precio Unitario", width=120)
    total_general_text = ft.Text(value=formatear_moneda(0), size=18, weight=ft.FontWeight.BOLD)

    tabla_items = ft.Column(spacing=5)

    def limpiar_campos():
        descripcion.value = ""
        cantidad.value = ""
        precio_unitario.value = ""
        descripcion.update()
        cantidad.update()
        precio_unitario.update()

    def agregar_item(e):
        # Limpiar colores previos
        descripcion.bgcolor = None
        cantidad.bgcolor = None
        precio_unitario.bgcolor = None
        descripcion.update()
        cantidad.update()
        precio_unitario.update()

        # Validaciones
        error = False
        if not descripcion.value.strip():
            descripcion.bgcolor = ft.Colors.RED_100
            error = True
        if not cantidad.value.strip() or not cantidad.value.isdigit() or int(cantidad.value) <= 0:
            cantidad.bgcolor = ft.Colors.RED_100
            error = True
        try:
            precio = float(precio_unitario.value.replace(",", "."))
            if precio <= 0:
                precio_unitario.bgcolor = ft.Colors.RED_100
                error = True
        except ValueError:
            precio_unitario.bgcolor = ft.Colors.RED_100
            error = True

        if error:
            descripcion.update()
            cantidad.update()
            precio_unitario.update()
            return  # No agrega el ítem hasta que todos los campos sean correctos

        # Si todo es válido, agregar el item
        try:
            cantidad_int = int(cantidad.value)
        except (ValueError, TypeError):
            print("Cantidad inválida (vacía o no numérica).")
            return
        total = round(cantidad_int * precio, 2)

        items_list.append({
            "descripcion": descripcion.value.strip(),
            "cantidad": int(cantidad.value),
            "precio_unitario": precio,
            "total": total
        })

        limpiar_campos()
        actualizar_tabla()

    def eliminar_item(idx):
        items_list.pop(idx)
        actualizar_tabla()

    def cargar_para_modificar(idx):
        item = items_list[idx]
        descripcion.value = item["descripcion"]
        cantidad.value = str(item["cantidad"])
        precio_unitario.value = str(item["precio_unitario"]).replace(".", ",")
        descripcion.update()
        cantidad.update()
        precio_unitario.update()
        items_list.pop(idx)
        actualizar_tabla()

    def actualizar_tabla():
        tabla_items.controls.clear()
        for idx, item in enumerate(items_list):
            fila = ft.Row(
                [
                    ft.Text(item["descripcion"], width=250),
                    ft.Text(str(item["cantidad"]), width=70),
                    ft.Text(formatear_moneda(item["precio_unitario"]), width=140),
                    ft.Text(formatear_moneda(item["total"]), width=120),
                    ft.ElevatedButton("Modificar", width=80, height=35, on_click=lambda e, i=idx: cargar_para_modificar(i)),
                    ft.ElevatedButton("Eliminar", width=80, height=35, on_click=lambda e, i=idx: eliminar_item(i))
                ],
                spacing=10
            )
            tabla_items.controls.append(fila)
        tabla_items.update()
        total_general = sum(item["total"] for item in items_list)
        total_general_text.value = formatear_moneda(total_general)
        total_general_text.update()

    boton_agregar = ft.ElevatedButton("Agregar Ítem", width=150, height=45, bgcolor=ft.Colors.GREEN_100, on_click=agregar_item)

    contenedor = ft.Container(
        content=ft.Column(
            [
                ft.Text("Ingreso de Ítems", size=22, weight=ft.FontWeight.BOLD),
                ft.Row([descripcion, cantidad, precio_unitario, boton_agregar], spacing=10),
                tabla_items,
                ft.Row([ft.Text("Total:", size=18, weight=ft.FontWeight.BOLD), total_general_text], alignment=ft.MainAxisAlignment.END)
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=20,
        width=800,
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.border_radius.all(12),
        shadow=ft.BoxShadow(color=ft.Colors.BLACK12, blur_radius=6, offset=ft.Offset(2,2)),
    )

    return contenedor, boton_agregar, items_list, total_general_text