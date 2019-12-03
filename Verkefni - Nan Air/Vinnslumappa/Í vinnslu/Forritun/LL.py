class LL_API():
    def create_trip(dict):
        return Trip(dict)

    def change_trip():
        return LL_Trips.changeTrip()

    def search_trip():
        return LL_Trips.searchTrip()

    def remove_trip():
        return LL_Trips.removeTrip()
    
    def create_plane(dict):
        return LL_Planes(dict)

    def change_plane():
        return LL_Planes.changePlane()

    def search_trip():
        return LL_Planes.searchPlane()

    def remove_trip():
        return LL_Planes.removePlane()

    def create_destination(dict):
        return LL_Destinations(dict)

    def change_destination():
        return LL_Destinations.changeDestination()

    def search_destination():
        return LL_Destinations.searchDestination()

    def remove_destination():
        return LL_Destinations.removeDestination()
    
    def create_destination(dict):
        return LL_Employee(dict)

    def change_destination():
        return LL_Employee.changeEmployee()

    def search_destination():
        return LL_Employee.searchEmployee()

    def remove_destination():
        return LL_Employee.removeEmployee()

    



class LL_Trips():

    def changeTrip():
        pass

    def searchTrip():
        pass

    def removeTrip():
        pass


class LL_Planes():

    def changePlane():
        pass

    def searchPlane():
        pass

    def removePlane():
        pass

class LL_Destinations():

    def changeDestination():
        pass

    def searchDestination():
        pass

    def removeDestination():
        pass

class LL_Employee():

    def changeEmployee():
        pass

    def searchEmployee():
        pass

    def removeEmployee():
        pass



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

    def __str__(self):
        return 'ID: {}'.format(self.__destination)

class Trip():

    def __init__(self, tripDict):
        
        self.__destination = tripDict["airportID"]
        self.__depart_Time_Home = tripDict["depart_Time"]
        self.__arrival_Time_Dest = tripDict["arrival_Time_Dest"]
        self.__depart_Time_Abr = tripDict["depart_Time_Abr"]
        self.__arrival_Time_Home = tripDict["arrival_Time_Home"]

class LL_API():
    def new_Employee(self, dict):
        return Destination.__init__()

def main():
    destinationDict = {"airportID": "LYR", "destination": "Longyearbyen", "country" : "Norway", "flightTime" : "XXX", "distance" : "1998", "emergencyContact" : "AntMan", "emergencyContactNumber" : "5559999" }
    destination = Destination(destinationDict)
    print(destination)

main() 