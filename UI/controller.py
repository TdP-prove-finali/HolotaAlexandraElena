import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def populated_ddFonteRinnovabile(self):
        fonti = self._model.getRenewableSource()
        for f in fonti:
            self._view._ddFonteRinnovabile.options.append(ft.dropdown.Option(key=f.id, text=f.tipo))
        self._view.update_page()

    def populated_ddAttributes(self):
        self._view._ddAttributes.options.append(ft.dropdown.Option(key="analisiGenerale", text="Analisi Generale"))
        opzioni = self._model.getAllOptions()
        for o in opzioni:
            self._view._ddAttributes.options.append(ft.dropdown.Option(key=o.attributes, text=o.attributi))
        self._view.update_page()

    def get_Analisi(self, e):
        pass




