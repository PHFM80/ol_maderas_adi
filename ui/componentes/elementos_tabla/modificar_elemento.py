import flet as ft
import sqlite3
import os



def cerrar_dialogo(page):
    if page.dialog:
        page.dialog.open = False
        page.update()

def mostrar_inputs_modificacion(page: ft.Page, contenedor, id_producto):
    try:
        id_producto = int(id_producto)
    except (ValueError, TypeError):
        contenedor.controls.clear()
        contenedor.controls.append(
            ft.Text("⚠ Por favor ingrese un número de item válido.", color=ft.Colors.RED)
        )
        page.update()
        return

    # Ruta base y DB
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../../../db/presupuesto.db")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT cantidad, descripcion, precio_unitario FROM detalle_producto WHERE id = ?",
            (id_producto,),
        )
        resultado = cursor.fetchone()
        conn.close()

        contenedor.controls.clear()

        if not resultado:
            contenedor.controls.append(
                ft.Text(f"❌ No se encontró ningún ítem con nro: {id_producto}.", color=ft.Colors.RED)
            )
            page.update()
            return

        cantidad_inicial, descripcion_inicial, precio_inicial = resultado

        cantidad_input = ft.TextField(
            label="Cantidad",
            value=str(cantidad_inicial),
            keyboard_type=ft.KeyboardType.NUMBER,
            width=150,
        )
        descripcion_input = ft.TextField(
            label="Descripción",
            value=descripcion_inicial,
            width=300,
        )
        precio_input = ft.TextField(
            label="Precio unitario",
            value=str(precio_inicial),
            keyboard_type=ft.KeyboardType.NUMBER,
            width=150,
        )

        def guardar_cambios(e):
            try:
                nueva_cantidad = int(cantidad_input.value)
                nueva_descripcion = descripcion_input.value.strip()
                nuevo_precio = float(precio_input.value)
                nuevo_total = nueva_cantidad * nuevo_precio

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE detalle_producto
                    SET cantidad = ?, descripcion = ?, precio_unitario = ?, total = ?
                    WHERE id = ?
                """, (nueva_cantidad, nueva_descripcion, nuevo_precio, nuevo_total, id_producto))
                conn.commit()
                conn.close()

                contenedor.controls.clear()
                contenedor.controls.append(
                    ft.Text(f"✅ Producto con item: {id_producto} actualizado correctamente.", color=ft.Colors.GREEN)
                )
                page.update()

            except Exception as err:
                contenedor.controls.append(
                    ft.Text(f"⚠ Error al guardar cambios: {err}", color=ft.Colors.RED)
                )
                page.update()

        contenedor.controls.extend([
            cantidad_input,
            descripcion_input,
            precio_input,
            ft.Row([
                ft.ElevatedButton("Guardar", on_click=guardar_cambios),
                ft.TextButton("Cancelar", on_click=lambda e: (contenedor.controls.clear(), page.update())),
            ], spacing=10)
        ])

        page.update()

    except Exception as e:
        contenedor.controls.clear()
        contenedor.controls.append(
            ft.Text(f"⚠ Error al cargar datos: {e}", color=ft.Colors.RED)
        )
        page.update()
