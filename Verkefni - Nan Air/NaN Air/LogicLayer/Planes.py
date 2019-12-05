class Planes ():

    def __init__ (self, planeDict):
        self.__insignia = planeDict["plane_insignia"]
        self.__typeID = planeDict["plane_type_ID"]
        self.__manufacturer = planeDict["plane_manufacturer"]
        self.__model = planeDict["plane_model"]
        self.__capacity = planeDict["plane_capacity"]

    def get_insignia(self):
        return self.__insignia

    def get_typeID(self):
        return self.__typeID

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity