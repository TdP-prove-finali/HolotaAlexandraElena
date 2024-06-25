import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddFonteRinnovabile = None
        self._ddAttributes = None



    def load_interface(self):
        # title
        self._title = ft.Text("Software per l’analisi statistica di sistemi energetici rinnovabili e valutazione degli investimenti per i clienti",
                              color="blue", size=24, text_align=ft.TextAlign.CENTER)
        self._page.controls.append(self._title)

        # row 1: scelta fonte rinnovabile e categorie da analizzare
        self._ddFonteRinnovabile = ft.Dropdown(label="Renewable energy system", width=250, options=[])
        self._ddAttributes = ft.Dropdown(label="Options", width=250, options=[])
        self._btnAnalisi = ft.ElevatedButton(text="Analisi", width=200, on_click=self._controller.get_Analisi)
        self.controller.populated_ddFonteRinnovabile()
        self.controller.populated_ddAttributes()

        row1 = ft.Row([self._ddFonteRinnovabile, self._ddAttributes, self._btnAnalisi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()