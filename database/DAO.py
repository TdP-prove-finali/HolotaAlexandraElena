from database.DB_connect import DBConnect
from model.fonteRinnovabile import FonteRinnovabile
from model.options import Options


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getRenewableSource():
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


