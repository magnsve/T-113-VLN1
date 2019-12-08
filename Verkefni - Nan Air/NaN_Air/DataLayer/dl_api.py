# Classes and Constants
from .dl_employee import DL_Employee
from .dl_planes import DL_Planes
from .dl_trips import DL_Trips
from .dl_destinations import DL_Destinations


#Classes 
class DL_API():
    ''' '''
    # Employees
    def get_employees(self):        
        return DL_Employee().getEmployees()

    def append_employee(self, employee_object):        
        return DL_Employee().appendEmployee(employee_object)
    
    def modify_employee(self, employee_object, index):
        return DL_Employee().modifyEmployee(employee_object, index)
    
    def get_headers(self):
        return DL_Employee().getHeaders()

    # Planes
    def get_planes(self):        
        return DL_Planes().get_planes()

    def append_planes(self, plane_object):        
        return DL_Planes().append_planes(plane_object)
    
    def modify_planes(self, plane_object, index):
        return DL_Planes().modify_planes(plane_object, index)
    
    def get_headers_plane(self):
        return DL_Planes().get_headers_plane()



    def get_trips(self):        
        return DL_Trips().get_trips()

    def append_trips(self, trip_object):        
        return DL_Trips().append_trips(trip_object)
    
    def modify_trips(self, trip_object, index):
        return DL_Trips().modify_trips(trip_object, index)
    
    def get_headers_trips(self):
        return DL_Trips().get_headers_trips()



    def get_destinations(self):        
        return DL_Destinations().get_destinations()

    def append_destinations(self, destination_object):        
        return DL_Destinations().append_destinations(destination_object)
    
    def modify_destinations(self, destination_object, index):
        return DL_Destinations().modify_destinations(destination_object, index)
    
    def get_headers_destinations(self):
        return DL_Destinations().get_headers_destinations()

#_______________________________________________________________________

    def close_file_EmployeeFilename(self):
        pass

    def createOutput_EmployeeFilename(self):
        pass
    def read_file_TripFilename(self):
        pass

    def close_file_TripFilename(self):
        pass

    def createOutput_TripFilename(self):
        pass

    def read_file_PlaneFilename(self):
        pass

    def close_file_PlaneFilename(self):
        pass

    def createOutput_PlaneFilename(self):
        pass

    def read_file_DestinationFilename(self):
        pass

    def close_file_DestinationFilename(self):
        pass

    def createOutput_DestiantionFilename(self):
        pass

    def read_file_EmployeeFilename(self):
        pass