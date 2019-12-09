#imports and constants
import csv
from ModelClasses.employee import Employee

#Classes

class DL_Employee():
    ''' '''
    FILE_NAME = 'DataLayer\\DL_Database\\Employees.csv'

    def getEmployees(self):
        _file = csv.DictReader(open(self.FILE_NAME,'r', encoding='utf-8-sig'))
        output = []
        for row in _file:
            data = Employee(row)
            output.append(data)
        return output

    def appendEmployee(self, employee_object):
        with open(self.FILE_NAME, 'a') as _file:
            _file.write(employee_object.__str__())
        return True        

    def modifyEmployee(self, employee_object, index):
        lines = open(self.FILE_NAME).read().splitlines()
        print(lines)
        print(employee_object.__str__())
        lines[index] = employee_object.__str__()
        open(self.FILE_NAME,'w').write('\n'.join(lines))
        return True
    
    def getHeaders(self):
        with open(self.FILE_NAME) as _file:
            dict_reader = csv.DictReader(_file)
            return dict_reader.fieldnames