# Imports and constants
from .ll_destinations import LL_Destinations
from .ll_employee import LL_Employee
from .ll_planes import LL_Planes
from .ll_trips import LL_Trips

# Classes
class LL_API():
    ''' Logic layer calls on methods in it's subclasses and returns them over to the interface layer'''

    def inactivate_employee(self, employee_object, index):
        return LL_Employee().inactivateEmployee(employee_object, index)
    
    def get_employee_header(self):
        return LL_Employee().get_headers()
    
    def search_employee(self, employee_object):
        return LL_Employee().searchEmployee(employee_object)

    def inactivate_destination(self, destination_object, index):
        return LL_Destinations().inactivateDestination(destination_object, index)
    
    def get_destination_header(self):
        return LL_Destinations().get_headers()
    
    def search_destination(self, destination_object):
        return LL_Destinations().search_destination(destination_object)

    def inactivate_trip(self, employee_object, index):
        return LL_Trips().inactivateTrip(trip_object, index)
    
    def get_trip_header(self):
        return LL_Trips().get_headers()
    
    def search_trip(self, employee_object):
        return LL_Trips().searchTrip(trip_object)

    def inactivate_plane(self, destination_object, index):
        return LL_Planes().inactivateplane(plane_object, index)
    
    def get_plane_header(self):
        return LL_Planes().get_headers()
    
    def search_plane(self, destination_object):
        return LL_Planes().search_plane(plane_object)


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