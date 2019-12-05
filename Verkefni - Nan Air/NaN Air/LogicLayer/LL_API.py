from LogicLayer import *

class LL_API():
    def create_trip(self, dict):
        return Trip(dict)

    def change_trip(self):
        return LL_Trips.changeTrip()

    def search_trip(self):
        return LL_Trips.searchTrip()

    def remove_trip(self):
        return LL_Trips.removeTrip()
    
    def create_plane(self, dict):
        return Planes(dict)

    def change_plane(self):
        return LL_Planes.changePlane()

    def search_trip(self):
        return LL_Planes.searchPlane()

    def remove_trip(self):
        return LL_Planes.removePlane()

    def create_destination(self, dict):
        return Destinations(dict)

    def change_destination(self):
        return LL_Destinations.changeDestination()

    def search_destination(self):
        return LL_Destinations.searchDestination()

    def remove_destination(self):
        return LL_Destinations.removeDestination()
    
    def create_destination(self, dict):
        return Employee(dict)

    def change_destination(self):
        return LL_Employee.changeEmployee()

    def search_destination(self):
        return LL_Employee.searchEmployee()

    def remove_destination(self):
        return LL_Employee.removeEmployee()