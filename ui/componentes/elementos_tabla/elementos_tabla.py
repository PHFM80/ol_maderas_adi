import flet as ft
import sqlite3
import os

from ui.componentes.elementos_tabla.form_detalle import FormDetalle
from ui.componentes.elementos_tabla.tabla_detalle import TablaDetalle
from ui.componentes.elementos_tabla.modificar_elemento import mostrar_inputs_modificacion

class ElementosTabla:
    def __init__(self, page):
        self.page = page
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../db/presupuesto.db")

        # Formulario para agregar productos
        self.formulario = FormDetalle(self.on_add_item)

        # Selector de moneda
        self.selector_moneda = ft.Dropdown(
            label="Moneda en la que se abona",
            width=200,
            options=[ft.dropdown.Option("Pesos"), ft.dropdown.Option("Dólares")],
            value=None,
            on_change=self.on_moneda_change,
        )

        self.btn_mostrar = ft.ElevatedButton("Mostrar productos agregados", on_click=self.on_mostrar_click)
        self.id_a_modificar = None

        self.contenedor_tabla = ft.Column()
        self.contenedor_edicion = ft.Column()  

        self.contenedor = ft.Container(
            content=ft.Column([
                ft.Text("Detalle de cotización", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10),
                self.selector_moneda,
                ft.Divider(height=20),
                self.formulario,
                ft.Divider(height=20),
                self.btn_mostrar,
                ft.Divider(height=30),

                self.contenedor_tabla,  # tabla cargada dinámicamente

                ft.Divider(height=30),
                ft.Text("Modificar producto", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("Debe ingresar el número de item que desea modificar", size=14, italic=True),
                ft.Row([
                    ft.TextField(
                        label="Item del producto",
                        width=150,
                        keyboard_type=ft.KeyboardType.NUMBER,
                        autofocus=False,
                        on_change=self.on_id_input_change,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.ElevatedButton("Modificar", on_click=self.on_modificar_click),
                ]),

                self.contenedor_edicion  
            ]),
            padding=20,
            border=ft.border.all(1, ft.Colors.GREY),
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY, offset=ft.Offset(2, 2)),
        )

    def on_moneda_change(self, e):
        moneda = e.control.value
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM moneda")
            cursor.execute("INSERT INTO moneda (moneda) VALUES (?)", (moneda,))
            conn.commit()
            conn.close()
        except Exception as err:
            print(f"Error al guardar moneda: {err}")
        self.page.update()

    def on_add_item(self):
        pass
        
        
    def on_mostrar_click(self, e):
        self.contenedor_tabla.controls.clear()
        tabla = TablaDetalle()
        tabla.refrescar()
        self.contenedor_tabla.controls.append(tabla)
        self.page.update()

    def on_id_input_change(self, e):
        try:
            self.id_a_modificar = int(e.control.value)
        except ValueError:
            self.id_a_modificar = None

    def on_modificar_click(self, e):
        if self.id_a_modificar is not None:
            # Limpiar antes de mostrar inputs
            self.contenedor_edicion.controls.clear()
            mostrar_inputs_modificacion(self.page, self.contenedor_edicion, self.id_a_modificar)
            self.page.update()


    def get_container(self):
        return self.contenedor
