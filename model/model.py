from database.DAO import DAO


class Model:
    def __init__(self):
        self._analisiMax = None
        self._analisiMin = None
        self._analisiAVG = None

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

    def analisiSpecifica(self, fonte, categoria):
        self._analisiMax = DAO.getMaxValueForType(fonte)
        self._analisiMin = DAO.getMinValueForType(fonte)
        self._analisiAVG = DAO.getAVGValueForType(fonte)

    def getAllRenewableSource(self):
        return DAO.getAllRenewableSource()

    def getAllOptions(self):
        return DAO.getAllOptions()