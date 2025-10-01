# ui/componentes/elementos_tabla/form_detalle.py

import flet as ft
from ui.componentes.elementos_tabla.guardar_detalle_producto import guardar_detalle_en_bd

class FormDetalle(ft.Container):
    def __init__(self, on_item_agregado):
        super().__init__()

        self.on_item_agregado = on_item_agregado

        self.input_cantidad = ft.TextField(label="Cantidad", width=100)
        self.input_descripcion = ft.TextField(label="Descripción", width=300)
        self.input_precio_unitario = ft.TextField(label="Precio Unitario", width=150)

        self.btn_agregar = ft.ElevatedButton(
            text="Agregar",
            on_click=self.agregar_item
        )

        self.content = ft.Row([
            self.input_cantidad,
            self.input_descripcion,
            self.input_precio_unitario,
            self.btn_agregar
        ])

    def agregar_item(self, e):
        try:
            cantidad = int(self.input_cantidad.value)
            descripcion = self.input_descripcion.value.strip()
            precio_unitario = round(float(self.input_precio_unitario.value), 2)
            total = round(cantidad * precio_unitario, 2)

            # Guardar en base de datos
            guardar_detalle_en_bd(cantidad, descripcion, precio_unitario, total)

            # Llamar al callback para refrescar tabla
            self.on_item_agregado()

            # Limpiar campos
            self.input_cantidad.value = ""
            self.input_descripcion.value = ""
            self.input_precio_unitario.value = ""
            self.update()

        except ValueError:
            print("⚠ Ingrese valores válidos para cantidad y precio unitario.")
