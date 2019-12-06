#imports and constants
import csv
from LogicLayer.ll_api import LL_API

#Classes

class DL_Employee():
    ''' '''
    FILE_NAME = 'Employees.csv'

    def getEmployees(self):
        _file = csv.DictReader(open(self.FILE_NAME))
        output = []
        for row in _file:
            data = LL_API.createEmployee(self, row)
            output.append(data)
        return output

    def appendEmployee(self, employee_object):
        with open(self.FILE_NAME, 'a') as _file:
            _file.write(employee_object.__str__())
        return True        

    def modifyDestinations(self, destination_object, index):
        pass