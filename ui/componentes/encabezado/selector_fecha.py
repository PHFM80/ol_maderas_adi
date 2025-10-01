# ui/componentes/encabezado/selector_fecha.py
import datetime
import flet as ft

class SelectorFecha(ft.Column):
    def __init__(self, page, on_date_selected):
        self.page = page
        self.on_date_selected = on_date_selected
        self.fecha_seleccionada = None  # para almacenar la fecha elegida

        self.selected_date = ft.Text()

        self.date_picker = ft.DatePicker(
            first_date=datetime.datetime(year=2020, month=1, day=1),
            last_date=datetime.datetime(year=2030, month=12, day=31),
            on_change=self.handle_change,
            on_dismiss=self.handle_dismissal,
        )

        self.page.overlay.append(self.date_picker)

        btn_open_picker = ft.ElevatedButton(
            "Seleccionar fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda _: self.abrir_picker()
        )

        super().__init__(
            controls=[btn_open_picker, self.selected_date],
            alignment=ft.MainAxisAlignment.START,
            spacing=5
        )

    def abrir_picker(self):
        self.date_picker.open = True
        self.page.update()

    def handle_change(self, e):
        self.fecha_seleccionada = e.control.value
        self.selected_date.value = f"Fecha seleccionada: {self.fecha_seleccionada.strftime('%d/%m/%Y')}"
        self.on_date_selected(self.fecha_seleccionada)
        self.page.update()

    def handle_dismissal(self, e):
        self.selected_date.value = "Selector de fecha cerrado sin seleccionar"
        self.page.update()
