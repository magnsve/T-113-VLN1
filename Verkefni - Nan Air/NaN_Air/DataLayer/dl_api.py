# Classes and Constants
from .dl_employee import DL_Employee



#Classes 
class DL_API():

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

    def get_employees(self):
        temp = DL_Employee()
        return temp.getEmployees()

    def append_employee(self, employee_object):
        temp = DL_Employee()
        return temp.appendEmployee(employee_object)
    
    def modify_employee(self, employee_object, index):
        temp = DL_Employee()
        return temp.modifyEmployee(employee_object, index)

    def close_file_EmployeeFilename(self):
        pass

    def createOutput_EmployeeFilename(self):
        pass