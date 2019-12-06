# Imports and constants
from .destination import Destination
from .plane import Plane
from .trip import Trip
from .employee import Employee
from .ll_destinations import LL_Destinations
from .ll_employee import LL_Employee
from .ll_lanes import LL_Planes
from .ll_trips import LL_Trips

# Classes
class LL_API():
    ''' '''
    # Destinations Model class
    def createDestination(self, __dict):
        return Destination(__dict)
    
    # Employee Model Class
    def createEmployee(self, __dict):
        return Employee(__dict)

    # Airplane Model Class
    def createPlane(self, __dict):
        return Plane(__dict)

    # Trip Model class
    def createTrip(self, __dict):
        return Trip(__dict)

    # def change_destination(self):
    #     return LL_Destination.changeDestination()

    # def search_destination(self):
    #     return LL_Destination.searchDestination()

    # def remove_destination(self):
    #     return LL_Destination.removeDestination() 

    # def create_trip(self, _dict):
    #     return Trip(_dict)

    # def change_trip(self):
    #     return LL_Trips.changeTrip()

    # def search_trip(self):
    #     return LL_Trips.searchTrip()

    # def remove_trip(self):
    #     return LL_Trips.removeTrip()
    
    # def create_plane(self, _dict):
    #     return Planes(_dict)

    # def change_plane(self):
    #     return LL_Planes.changePlane()

    # def search_trip(self):
    #     return LL_Planes.searchPlane()

    # def remove_trip(self):
    #     return LL_Planes.removePlane()    
    
    # def create_destination(self, _dict):
    #     return Employee(_dict)

    # def change_destination(self):
    #     return LL_Employee.changeEmployee()

    # def search_destination(self):
    #     return LL_Employee.searchEmployee()

    # def remove_destination(self):
    #     return LL_Employee.removeEmployee()