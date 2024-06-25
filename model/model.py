from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getRenewableSource(self):
        return DAO.getRenewableSource()

    def getAllOptions(self):
        return DAO.getAllOptions()

