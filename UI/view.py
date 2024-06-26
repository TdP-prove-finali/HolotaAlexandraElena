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
        self._analisi = None
        self._ddFonteRinnovabile = None
        self._ddAttributes = None
        self._btnAnalisi = None
        self._txt_resultAnalisi = None
        self._soluzione = None
        self._txtImporto = None
        self._txtCapacita = None
        self._btnSoluzione = None
        self._txt_resultSoluzione = None


    def load_interface(self):
        # title
        self._title = ft.Text("Software per l’analisi statistica di sistemi energetici rinnovabili e valutazione degli investimenti per i clienti",
                              color="blue", size=24, text_align=ft.TextAlign.CENTER)
        self._page.controls.append(self._title)

        self._ddFonteRinnovabile = ft.Dropdown(label="Sistema energetico rinnovabile", width=300)
        self.controller.populated_ddFonteRinnovabile()
        row = ft.Row([self._ddFonteRinnovabile], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row)

        # row 1: scelta fonte rinnovabile e categorie da analizzare

        self._analisi = ft.Text("Analisi Preliminare", color="green", size=20)
        self._ddAttributes = ft.Dropdown(label="Opzioni", width=450)
        self._btnAnalisi = ft.ElevatedButton(text="Analisi", width=100, on_click=self._controller.get_Analisi)
        self.controller.populated_ddAttributes()

        row1 = ft.Row([self._analisi, self._ddAttributes, self._btnAnalisi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # row 2 : risultati analisi
        self._txt_resultAnalisi = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True, height=250)
        row2 = ft.Row([self._txt_resultAnalisi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # row 3 : soluzione per il cliente
        self._soluzione = ft.Text("Soluzione per il cliente", color="green", size=20)
        self._txtImporto = ft.TextField(label="Investimento iniziale (in $)", width=200, disabled=True)
        self._txtCapacita = ft.TextField(label="Capacità minima (in MW)", width=200, disabled=True)
        self._btnSoluzione = ft.ElevatedButton(text="Trova", width=100, disabled=True, on_click=self._controller.get_SoluzioneCliente)

        row3 = ft.Row([self._soluzione, self._txtImporto, self._txtCapacita, self._btnSoluzione], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # row 4 : risultati soluzione per il cliente
        self._txt_resultSoluzione = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        row4 = ft.Row([self._txt_resultSoluzione], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)




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