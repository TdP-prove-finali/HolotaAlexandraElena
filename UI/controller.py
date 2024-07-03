import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._analisi = None
        self._analisiValore = None
        self._fonteRinnovabile = None

    def get_SoluzioneCliente(self, e):
        self._view._txt_resultSoluzione.controls.clear()
        if self._view._txtImporto.value != "":
            try:
                importo = float(self._view._txtImporto.value)
            except ValueError:
                self._view.txt_resultSoluzione.controls.append(ft.Text("Investimento iniziale non valido"))
                self._view.update_page()
                return
        else:
            self._view.txt_resultSoluzione.controls.append(ft.Text("Inserire l' investimento iniziale desiderato"))
            self._view.update_page()
            return
        if self._view._txtCapacita != "":
            try:
                capacita = float(self._view._txtCapacita.value)
            except ValueError:
                self._view.txt_resultSoluzione.controls.append(ft.Text("Capacità non valida"))
                self._view.update_page()
                return
        else:
            self._view.txt_resultSoluzione.controls.append(ft.Text("Inserire la capacità desidera"))
            self._view.update_page()
            return

        if self._fonteRinnovabile == None:
            self._view.txt_resultSoluzione.controls.append(ft.Text("Inserire la fonte rinnovabile"))
            self._view.update_page()
            return

        self.grafo = self._model.buildGrafo(self._fonteRinnovabile, importo, capacita)
        # self._view._txt_resultSoluzione.controls.append(ft.Text("Grafo correttamente creato."))
        n, a = self._model.getGraphDetails()
        # self._view._txt_resultSoluzione.controls.append(ft.Text(
        #    f"Il grafo è costituito di {n} nodi e {a} archi."))

        self._model.getBestNodes()

        if len(self._model.bestNodes) != 0:
            self._view._txt_resultSoluzione.controls.append(ft.Text(f"Abbiamo trovato {len(self._model.bestNodes)} soluzioni ottime: "))
            for n in self._model.bestNodes:
                self._view._txt_resultSoluzione.controls.append(ft.Text(
                    f"{self._model._idMap[n].id} - Investimento inziale (USD): {self._model._idMap[n].Initial_Investment_USD} e Capacità installata (MW) : {self._model._idMap[n].Installed_Capacity_MW}"))
        else:
            self._view._txt_resultSoluzione.controls.append(ft.Text(f"Non abbiamo trovato nessuna soluzione "))


        self._view.update_page()


    def get_Analisi(self, e):
        self._view._txt_resultAnalisi.controls.clear()
        if self._fonteRinnovabile is not None:
            if self._analisi == "Analisi Generale" or self._analisi==None:
                minimo = self._model.analisiGeneraleMin(self._fonteRinnovabile)
                massimo = self._model.analisiGeneraleMax(self._fonteRinnovabile)
                media = self._model.analisiGeneraleAVG(self._fonteRinnovabile)
                self._view._txt_resultAnalisi.controls.append(ft.Text("Analisi Generale: "))
                self._view._txt_resultAnalisi.controls.append(ft.Text("I valori di minimo sono: "))
                self.stampaValoriAnalisi(minimo)
                self._view._txt_resultAnalisi.controls.append(ft.Text("---------------------------"))
                self._view._txt_resultAnalisi.controls.append(ft.Text("I valori di massimo sono: "))
                self.stampaValoriAnalisi(massimo)
                self._view._txt_resultAnalisi.controls.append(ft.Text("---------------------------"))
                self._view._txt_resultAnalisi.controls.append(ft.Text("I valori di medi sono: "))
                self.stampaValoriAnalisi(media)
            else:
                minimo = self._model.analisiSpecificaMin(self._fonteRinnovabile, self._analisi)
                massimo = self._model.analisiSpecificaMax(self._fonteRinnovabile, self._analisi)
                media = self._model.analisiSpecificaAVG(self._fonteRinnovabile, self._analisi)
                self._view._txt_resultAnalisi.controls.append(ft.Text(f"Analisi specifica per la categoria {self._analisiValore}: "))
                self._view._txt_resultAnalisi.controls.append(ft.Text(f"Il valore minimo trovato è: {minimo}"))
                self._view._txt_resultAnalisi.controls.append(ft.Text(f"Il valore massimo trovato è: {massimo}"))
                self._view._txt_resultAnalisi.controls.append(ft.Text(f"Il valore medio calcoltao è: {media} "))

            self._view._txtImporto.disabled = False
            self._view._txtCapacita.disabled = False
            self._view._btnSoluzione.disabled = False
            self._view.update_page()
        else:
            self._view._txt_resultAnalisi.controls.append(ft.Text(f"Non è stata scelto un sistema energetico rinnovabile da analizzare"))
            self._view.update_page()
            return



    def populated_ddFonteRinnovabile(self):
        fonti = self._model.getAllRenewableSource()
        for f in fonti:
            self._view._ddFonteRinnovabile.options.append(ft.dropdown.Option(data=f.id, on_click=self.readDDFonteRinnovabile, text=f.tipo))
        self._view.update_page()

    def populated_ddAttributes(self):
        self._view._ddAttributes.options.append(ft.dropdown.Option(
            data="Analisi Generale",
            on_click=self.readDDAnalisi,
            text="Analisi Generale"))
        opzioni = self._model.getAllOptions()
        for o in opzioni:
            self._view._ddAttributes.options.append(ft.dropdown.Option(
                data=o.attributes,on_click=self.readDDAnalisi, text=o.attributi
            ))
        self._view.update_page()

    def readDDAnalisi(self, e):
        if e.control.data is None:
            self._analisi = None
            self._analisiValore = None
        else:
            self._analisi = e.control.data
            self._analisiValore = self._view._ddAttributes.value

    def readDDFonteRinnovabile(self, e):
        if e.control.data is None:
            self._fonteRinnovabile = None
        else:
            self._fonteRinnovabile = e.control.data

    def stampaValoriAnalisi(self, valori):
        for k in valori.keys():
            self._view._txt_resultAnalisi.controls.append(
                ft.Text(f"{k}: {valori[k]}")
            )



