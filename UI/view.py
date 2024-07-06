import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Software Alexandra Elena Holota"
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
                              color="blue", size=24, weight="bold", text_align=ft.TextAlign.CENTER)
        self._page.controls.append(self._title)

        self._ddFonteRinnovabile = ft.Dropdown(label="Sistema energetico rinnovabile", width=400, )
        self.controller.populated_ddFonteRinnovabile()
        row = ft.Row([self._ddFonteRinnovabile], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row)

        # row 1: scelta fonte rinnovabile e categorie da analizzare

        self._analisi = ft.Text("Analisi Preliminare", color="#2E8B57", weight="bold", size=20)
        self._ddAttributes = ft.Dropdown(label="Opzioni", width=480)
        self._btnAnalisi = ft.ElevatedButton(text="Analisi", width=100, on_click=self._controller.get_Analisi)
        self.controller.populated_ddAttributes()

        row1 = ft.Row([self._analisi, self._ddAttributes, self._btnAnalisi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)


        # row 2 : soluzione per il cliente
        self._soluzione = ft.Text("Soluzione al cliente", color="#2E8B57", weight="bold", size=20)
        self._txtImporto = ft.TextField(label="Investimento iniziale ($)", width=230, disabled=True)
        self._txtCapacita = ft.TextField(label="Capacità minima (MW)", width=230, disabled=True)
        self._btnSoluzione = ft.ElevatedButton(text="Trova", width=100, disabled=True, on_click=self._controller.get_SoluzioneCliente)

        row2 = ft.Row([self._soluzione, self._txtImporto, self._txtCapacita, self._btnSoluzione], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self._txt_resultAnalisi = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._txt_resultSoluzione = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._txt_resultAnalisi.controls.append(ft.Text("Risultati Analisi", weight="bold", size=14))
        self._txt_resultSoluzione.controls.append(ft.Text("Soluzione per il cliente", weight="bold", size=14))

        container1 = ft.Container(
            content=self._txt_resultAnalisi,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_200,
            width=400,
            height=450,
            border_radius=10,
        )
        container2 = ft.Container(
            content=self._txt_resultSoluzione,
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_200,
            width=400,
            height=450,
            border_radius=10,
        )

        row3 = ft.Row([container1, container2],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                      spacing=50)
        self._page.controls.append(row3)


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