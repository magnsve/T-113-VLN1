# Imports and constants

# Classes
class Destination():
    def __init__(self, destinationDict):
        self.__airportId = destinationDict["airportID"]
        self.__destination = destinationDict["destination"]
        self.__country = destinationDict["country"]
        self.__flightTime = destinationDict["flightTime"]
        self.__distance = destinationDict["distance"]
        self.__emergencyContact = destinationDict["emergencyContact"]
        self.__emergencyContactNumber = destinationDict["emergencyContactNumber"]

    def get_airportID(self):        
        return self.__airportId

    def get_destination(self):
        return self.__destination
    
    def get_country(self):
        return self.__country

    def get_flightTime(self):
        return self.__flightTime

    def get_distance(self):
        return self.__distance

    def get_emergencyContact(self):
        return self.__emergencyContact

    def get_emergencyContactNumber(self):
        return self.__emergencyContactNumber