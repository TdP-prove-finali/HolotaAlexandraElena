from itertools import combinations

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._analisiMax = None
        self._analisiMin = None
        self._analisiAVG = None

        self._grafo = nx.Graph()
        self._idMapNodi = {}
        self._idMap = {}

        self.bestNodes = []
        self.bestScore = float('inf')

    def getBestNodes(self):
        self.bestNodes = []
        self.bestScore = float('inf')
        for node in self._idMapNodi.keys():
            parziale = [node]
            visited = set(parziale)
            self.ricorsione(parziale, visited)
        if len(self._idMapNodi.keys()) <= 3:
            self.bestNodes = list(self._idMapNodi.keys())
            self.bestScore = sum(self._idMapNodi[nodo] for nodo in self._idMapNodi.keys())

    def ricorsione(self, parziale, visitati):
        ultimo = parziale[-1]
        vicini = self.viciniAmmessi(ultimo, visitati)
        # Se abbiamo già tre nodi, confrontiamo il loro punteggio totale con il bestScore
        if len(parziale) == 3 :
            peso = sum(self._idMapNodi[nodo] for nodo in parziale)
            if peso < self.bestScore:
                self.bestScore = peso
                self.bestNodes = parziale[:]
            return
        # Ricorsione sui vicini
        for v in vicini:
            visitati.add(v)
            parziale.append(v)
            self.ricorsione(parziale, visitati)
            parziale.pop()
            visitati.remove(v)

    def viciniAmmessi(self, ultimo, visitati):
        if ultimo not in self._grafo:
            return []
        vicini = self._grafo.neighbors(ultimo)
        risultati = []
        for v in vicini:
            if v not in visitati and self._idMapNodi[v] <= self._idMapNodi[ultimo]:
                risultati.append(v)
        return risultati


    def buildGrafo(self, fonte, prezzo, capacita):
        self._grafo.clear()
        #aggiungi nodi
        self.nodes = DAO.getNodes(fonte, prezzo, capacita)
        self._idMap = {x.id: x for x in self.nodes}
        self._idMapNodi = {x.id: (x.Initial_Investment_USD/x.Installed_Capacity_MW) for x in self.nodes}
        self._grafo.add_nodes_from(self._idMapNodi.keys())
        #aggiungi archi
        self.edges = combinations(self._idMapNodi.keys(), 2)
        self._grafo.add_edges_from(self.edges)

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def analisiGeneraleMax(self, fonte):
        self._analisiMax = DAO.getMaxValueForType(fonte)
        massimo = {"Capacità Installata (MW)": self._analisiMax["Installed_Capacity_MW"],
                   "Produzione di Energia (MWh)": self._analisiMax["Energy_Production_MWh"],
                   "Consumo di Energia (MWh)": self._analisiMax["Energy_Consumption_MWh"],
                   "Capacità di Stoccaggio di Energia (MWh)": self._analisiMax["Energy_Storage_Capacity_MWh"],
                   "Investimento Iniziale (USD)": self._analisiMax["Initial_Investment_USD"],
                    "Indice di Riduzione dell'Inquinamento Atmosferico": self._analisiMax["Air_Pollution_Reduction_Index"]}
        return massimo

    def analisiGeneraleMin(self, fonte):
        self._analisiMin = DAO.getMinValueForType(fonte)
        minimo = {"Capacità Installata (MW)": self._analisiMin["Installed_Capacity_MW"],
                  "Produzione di Energia (MWh)": self._analisiMin["Energy_Production_MWh"],
                  "Consumo di Energia (MWh)": self._analisiMin["Energy_Consumption_MWh"],
                  "Capacità di Stoccaggio di Energia (MWh)": self._analisiMin["Energy_Storage_Capacity_MWh"],
                  "Investimento Iniziale (USD)": self._analisiMin["Initial_Investment_USD"],
                  "Indice di Riduzione dell'Inquinamento Atmosferico": self._analisiMin["Air_Pollution_Reduction_Index"]}
        return minimo

    def analisiGeneraleAVG(self, fonte):
        self._analisiAVG = DAO.getAVGValueForType(fonte)
        media = {"Capacità Installata (MW)": self._analisiAVG["Installed_Capacity_MW"],
                 "Produzione di Energia (MWh)": self._analisiAVG["Energy_Production_MWh"],
                 "Consumo di Energia (MWh)": self._analisiAVG["Energy_Consumption_MWh"],
                 "Capacità di Stoccaggio di Energia (MWh)": self._analisiAVG["Energy_Storage_Capacity_MWh"],
                 "Investimento Iniziale (USD)": self._analisiAVG["Initial_Investment_USD"],
                "Indice di Riduzione dell'Inquinamento Atmosferico": self._analisiAVG["Air_Pollution_Reduction_Index"]}
        return media

    def analisiSpecificaMax(self, fonte, categoria):
        self._analisiMax = DAO.getMaxValueForType(fonte)
        return self._analisiMax[categoria]

    def analisiSpecificaMin(self, fonte, categoria):
        self._analisiMin = DAO.getMinValueForType(fonte)
        return self._analisiMin[categoria]

    def analisiSpecificaAVG(self, fonte, categoria):
        self._analisiAVG = DAO.getAVGValueForType(fonte)
        return self._analisiAVG[categoria]

    def getAllRenewableSource(self):
        return DAO.getAllRenewableSource()

    def getAllOptions(self):
        return DAO.getAllOptions()