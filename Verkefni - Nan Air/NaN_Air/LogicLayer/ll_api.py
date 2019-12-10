# Imports and constants
from .ll_destinations import LL_Destinations
from .ll_employee import LL_Employee
from .ll_planes import LL_Planes
from .ll_trips import LL_Trips
from DataLayer.dl_api import DL_API

# Classes
class LL_API():
    ''' Logic layer calls on methods in it's subclasses and returns them over to the interface layer'''

    # Emmployees
    def edit_employee(self, employeeEditObject, index):
        return LL_Employee().edit_employee_object(employeeEditObject, index)
    
    def get_employee_header(self):
        return LL_Employee().get_employee_file_headers()
    
    def search_employee(self, employee_object):
        return LL_Employee().searchEmployee(employee_object)
    
    def find_employee_index(self, employee_object):
        return LL_Employee().find_index_in_database(employee_object)
    
    def new_employee(self, employee_object):
        return LL_Employee().add_employee(employee_object)
    
    # Destination
    def edit_destination(self, destination_object, index):
        return LL_Destinations().edit_employee_object(destination_object, index)

    def get_destination_header(self):
        return LL_Destinations().get_destination_file_headers()
    
    def search_destination(self, destination_object):
        return LL_Destinations().search_destination(destination_object)
    
    def find_destination_index(self, destination_object):
        return LL_Destinations().find_index_in_database(destination_object)
    
    def new_destination(self, destination_object):
        return LL_Destinations().add_destination(destination_object)

    # Trips
    def edit_trips(self, trip_object, index):
        return LL_Trips().edit_trip_object(trip_object, index)
    
    def get_trips_header(self):
        return LL_Trips().get_trips_file_headers()
    
    def search_trips(self, trip_object):
        return LL_Trips().search_trips(trip_object)

    def find_trips_index(self, trip_object):
        return LL_Trips().find_index_in_database(trip_object)
    
    def new_trips(self, trip_object):
        return LL_Trips().add_trip(trip_object)

    # Planes
    def edit_planes(self, plane_object, index):
        return LL_Planes().edit_plane_object(plane_object, index)
    
    def get_planes_header(self):
        return LL_Planes().get_plane_file_headers()
    
    def search_planes(self, plane_object):
        return LL_Planes().search_plane(plane_object)
    
    def find_planes_index(self, plane_object):
        return LL_Planes().find_index_in_database(plane_object)
    
    def new_planes(self, plane_object):
        return LL_Planes().add_plane(plane_object)