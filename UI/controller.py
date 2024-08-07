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
        importo = -1
        capacita = -1
        self._view._txt_resultSoluzione.controls.clear()
        if self._view._txtImporto.value != "" and self._view._txtCapacita.value != "" :
            try:
                importo = float(self._view._txtImporto.value)
            except ValueError:
                self._view._txt_resultSoluzione.controls.append(
                    ft.Text("Investimento iniziale non valido, inserire un importo"))
                self._view.update_page()
                return
            try:
                capacita = float(self._view._txtCapacita.value)
            except ValueError:
                self._view._txt_resultSoluzione.controls.append(
                    ft.Text("Capacità non valida"))
                self._view.update_page()
                return
        elif self._view._txtImporto.value == "" or self._view._txtCapacita.value == ""  :
            self._view._txt_resultSoluzione.controls.append(
                ft.Text("Inserire i dati richiesti"))
            self._view.update_page()
            return

        if self._fonteRinnovabile == None:
            self._view._txt_resultSoluzione.controls.append(
                ft.Text("Inserire la fonte rinnovabile"))
            self._view.update_page()
            return

        self.grafo = self._model.buildGrafo(self._fonteRinnovabile, importo, capacita)

        self._model.getBestNodes()

        if len(self._model.bestNodes) != 0:
            self._view._txt_resultSoluzione.controls.append(
                ft.Text(f"Abbiamo trovato {len(self._model.bestNodes)} soluzioni ottime: "))
            for n in self._model.bestNodes:
                self._view._txt_resultSoluzione.controls.append(ft.Text(
                    f"{self._model._idMap[n].id} -  "
                    f"Investimento inziale (USD): {self._model._idMap[n].Initial_Investment_USD} \n "
                    f"Capacità installata (MW) : {self._model._idMap[n].Installed_Capacity_MW} \n "
                    f"Indice di riduzione dell’inquinamento atmosferico: "
                    f"{self._model._idMap[n].Air_Pollution_Reduction_Index}  "))
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
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("Analisi Generale: "))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("I valori minimi sono: "))
                self.stampaValoriAnalisi(minimo)
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("---------------------------"))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("I valori massimi sono: "))
                self.stampaValoriAnalisi(massimo)
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("---------------------------"))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text("I valori medi sono: "))
                self.stampaValoriAnalisi(media)
            else:
                minimo = self._model.analisiSpecificaMin(self._fonteRinnovabile, self._analisi)
                massimo = self._model.analisiSpecificaMax(self._fonteRinnovabile, self._analisi)
                media = self._model.analisiSpecificaAVG(self._fonteRinnovabile, self._analisi)
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text(f"Analisi specifica per la categoria {self._view._ddAttributes.value}: "))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text(f"Il valore minimo trovato è: {minimo}"))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text(f"Il valore massimo trovato è: {massimo}"))
                self._view._txt_resultAnalisi.controls.append(
                    ft.Text(f"Il valore medio calcoltao è: {media} "))

            self._view._txtImporto.disabled = False
            self._view._txtCapacita.disabled = False
            self._view._btnSoluzione.disabled = False
            self._view.update_page()
        else:
            self._view._txt_resultAnalisi.controls.append(
                ft.Text(f"Non è stata scelto un sistema energetico rinnovabile da analizzare"))
            self._view.update_page()
            return


    def populated_ddFonteRinnovabile(self):
        fonti = self._model.getAllRenewableSource()
        for f in fonti:
            self._view._ddFonteRinnovabile.options.append(
                ft.dropdown.Option(
                    data=f.id, on_click=self.readDDFonteRinnovabile,
                    text=f.tipo))
        self._view.update_page()

    def populated_ddAttributes(self):
        self._view._ddAttributes.options.append(
            ft.dropdown.Option(
                data="Analisi Generale",
                on_click=self.readDDAnalisi,
                text="Analisi Generale"))
        opzioni = self._model.getAllOptions()
        for o in opzioni:
            self._view._ddAttributes.options.append(
                ft.dropdown.Option(
                    data=o.attribute,
                    text=o.attributo,
                    on_click=self.readDDAnalisi
            ))
        self._view.update_page()

    def readDDFonteRinnovabile(self, e):
        if e.control.data is None:
            self._fonteRinnovabile = None
        else:
            self._fonteRinnovabile = e.control.data

    def readDDAnalisi(self, e):
        if e.control.data is None:
            self._analisi = None
        else:
            self._analisi = e.control.data


    def stampaValoriAnalisi(self, valori):
        for k in valori.keys():
            self._view._txt_resultAnalisi.controls.append(
                ft.Text(f"{k}: {valori[k]}")
            )




