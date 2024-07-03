from database.DB_connect import DBConnect
from model.fonteRinnovabile import FonteRinnovabile
from model.options import Options
from model.sistemaEnergeticoRinnovabile import SistemaEnergeticoRinnovabile


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllRenewableSource():
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = 'SELECT * FROM RenewableSource'
            cursor.execute(query,)
            for row in cursor:
                result.append(FonteRinnovabile(row['id'], row['tipo']))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None
    @staticmethod
    def getAllOptions():
        cnx = DBConnect.get_connection()
        if cnx is not None:
            result = []
            cursor = cnx.cursor(dictionary=True)
            query = 'SELECT * FROM Options'
            cursor.execute(query, )
            for row in cursor:
                result.append(Options(row['attributes'], row['attributi']))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getMinValueForType(fonte):
        cnx = DBConnect.get_connection()
        if cnx is not None:

            cursor = cnx.cursor(dictionary=True)
            query = '''SELECT MIN(Installed_Capacity_MW) as Installed_Capacity_MW, MIN(Energy_Production_MWh) as Energy_Production_MWh, MIN(Energy_Consumption_MWh) as Energy_Consumption_MWh, MIN(Energy_Storage_Capacity_MWh) as Energy_Storage_Capacity_MWh, MIN(Storage_Efficiency_Percentage) as Storage_Efficiency_Percentage, MIN(Initial_Investment_USD) as Initial_Investment_USD, MIN(GHG_Emission_Reduction_tCO2e) as GHG_Emission_Reduction_tCO2e, MIN(Air_Pollution_Reduction_Index) as Air_Pollution_Reduction_Index, MIN(Jobs_Created) as Jobs_Created 
                        FROM RenewableEnergySystems res 
                        WHERE Type_of_Renewable_Energy = %s'''
            cursor.execute(query, (fonte,))
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getMaxValueForType(fonte):
        cnx = DBConnect.get_connection()
        if cnx is not None:

            cursor = cnx.cursor(dictionary=True)
            query = '''SELECT MAX(Installed_Capacity_MW) as Installed_Capacity_MW, MAX(Energy_Production_MWh) as Energy_Production_MWh, MAX(Energy_Consumption_MWh) as Energy_Consumption_MWh, MAX(Energy_Storage_Capacity_MWh) as Energy_Storage_Capacity_MWh, MAX(Storage_Efficiency_Percentage) as Storage_Efficiency_Percentage, MAX(Initial_Investment_USD) as Initial_Investment_USD, MAX(GHG_Emission_Reduction_tCO2e) as GHG_Emission_Reduction_tCO2e, MAX(Air_Pollution_Reduction_Index) as Air_Pollution_Reduction_Index, MAX(Jobs_Created) as Jobs_Created  
                        FROM RenewableEnergySystems res 
                        WHERE Type_of_Renewable_Energy = %s'''
            cursor.execute(query,(fonte,))
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getAVGValueForType(fonte):
        cnx = DBConnect.get_connection()
        if cnx is not None:

            cursor = cnx.cursor(dictionary=True)
            query = '''  SELECT AVG(Installed_Capacity_MW) as Installed_Capacity_MW, AVG(Energy_Production_MWh) as Energy_Production_MWh, AVG(Energy_Consumption_MWh) as Energy_Consumption_MWh, AVG(Energy_Storage_Capacity_MWh) as Energy_Storage_Capacity_MWh, AVG(Storage_Efficiency_Percentage) as Storage_Efficiency_Percentage, AVG(Initial_Investment_USD) as Initial_Investment_USD, AVG(GHG_Emission_Reduction_tCO2e) as GHG_Emission_Reduction_tCO2e, AVG(Air_Pollution_Reduction_Index) as Air_Pollution_Reduction_Index, AVG(Jobs_Created) as Jobs_Created
                         FROM RenewableEnergySystems res 
                         WHERE Type_of_Renewable_Energy = %s'''
            cursor.execute(query,(fonte,))
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getNodes(fonte, prezzo, capacita):
        cnx = DBConnect.get_connection()
        if cnx is not None:

            result = []

            cursor = cnx.cursor(dictionary=True)
            query = '''  SELECT *
                        FROM RenewableEnergySystems res 
                        WHERE res.Type_of_Renewable_Energy = %s and res.Initial_Investment_USD <= %s and res.Installed_Capacity_MW >= %s'''
            cursor.execute(query, (fonte,prezzo, capacita))
            for row in cursor:
                result.append(SistemaEnergeticoRinnovabile(**row))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None


