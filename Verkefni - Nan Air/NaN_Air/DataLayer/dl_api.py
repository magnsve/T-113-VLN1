# Classes and Constants
from .dl_employee import DL_Employee
from .dl_planes import DL_Planes
from .dl_trips import DL_Trips
from .dl_destinations import DL_Destinations

#Classes 
class DL_API():
    ''' This Class is a handler for all classes in the DataLayer. 
        It has 16 methods, 4 from each; Employees, Planes, Trips and Destinations. '''

    # Employees
    def get_employees(self):        
        return DL_Employee().getEmployees()

    def append_employee(self, employee_object):        
        return DL_Employee().appendEmployee(employee_object)
    
    def modify_employee(self, employee_object, index):
        return DL_Employee().modifyEmployee(employee_object, index)
    
    def get_employee_headers(self):
        return DL_Employee().getEmployeeHeaders()

    # Planes
    def get_planes(self):
        return DL_Planes().getPlanes()

    def append_planes(self, plane_object):        
        return DL_Planes().appendPlanes(plane_object)
    
    def modify_planes(self, plane_object, index):
        return DL_Planes().modifyPlanes(plane_object, index)
    
    def get_plane_headers(self):
        return DL_Planes().getPlanesHeaders()

    # Trips
    def get_trips(self):        
        return DL_Trips().getTrips()

    def append_trips(self, trip_object):        
        return DL_Trips().appendTrips(trip_object)
    
    def modify_trips(self, trip_object, index):
        return DL_Trips().modifyTrip(trip_object, index)
    
    def get_trips_headers(self):
        return DL_Trips().getTripsHeaders()

    # Destinations
    def get_destinations(self):        
        return DL_Destinations().getDestinations()

    def append_destinations(self, destination_object):        
        return DL_Destinations().appendDestinations(destination_object)
    
    def modify_destinations(self, destination_object, index):
        return DL_Destinations().modifyDestinations(destination_object, index)
    
    def get_destinations_headers(self):
        return DL_Destinations().getDestinationsHeaders()