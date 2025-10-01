# ui/componentes/elementos_tabla/tabla_detalle.py

import flet as ft
import sqlite3
import os

class TablaDetalle(ft.Container):
    def __init__(self):
        super().__init__()
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Item")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Descripción")),
                ft.DataColumn(ft.Text("Precio Unitario")),
                ft.DataColumn(ft.Text("Total")),
            ],
            rows=[],
        )
        self.content = self.table



    def refrescar(self):
        self.table.rows.clear()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "../../../db/presupuesto.db")

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, cantidad, descripcion, precio_unitario, total FROM detalle_producto")
            registros = cursor.fetchall()
            conn.close()

            for fila in registros:
                self.table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(fila[0]))),
                            ft.DataCell(ft.Text(str(fila[1]))),
                            ft.DataCell(ft.Text(fila[2])),
                            ft.DataCell(ft.Text(f"{fila[3]:.2f}")),
                            ft.DataCell(ft.Text(f"{fila[4]:.2f}")),
                        ]
                    )
                )
        except Exception as e:
            print(f"Error al cargar detalle: {e}")

