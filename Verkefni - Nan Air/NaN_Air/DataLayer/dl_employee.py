#imports and constants
import csv, codecs
from ModelClasses.employee import Employee

#Classes
class DL_Employee():
    ''' This class handles the database for Employeea. It has four methods:
        
        1) getEmployees:       This method reads the database and returns each line as an Employee object.
        2) appendEmployee:     This method appends an Employee object to the bottom of the database.
        3) modifyEmployee:     This method writes over an entry in the database. 
        4) getEmployeeHeaders: This method returns a list with the header row. '''

    FILE_NAME = 'DataLayer\\DL_Database\\Employees.csv'
    ENCODING = 'utf-8'

    def getEmployees(self):
        output = []
        with codecs.open(self.FILE_NAME, 'r', self.ENCODING) as _file:
            reader = csv.reader(_file)
            headers = next(reader)
            for row in reader:                
                row_dict = dict(zip(headers,row))
                employee_from_row = Employee(row_dict)
                output.append(employee_from_row)
        return output

    def appendEmployee(self, employee_object):
        with codecs.open(self.FILE_NAME, 'a', self.ENCODING) as _file:
            _file.write(employee_object.__str__())
        return True   

    def modifyEmployee(self, employee_object, index):
        list_of_employees = self.getEmployees()
        headers = self.getEmployeeHeaders()
        with codecs.open(self.FILE_NAME, 'w', self.ENCODING) as _file:
            writer = csv.writer(_file)
            list_of_employees[index] = employee_object
            output = [headers]
            for employee in list_of_employees:
                value_list = employee.__str__().split(',')
                output.append(value_list)
            for row in output:
                writer.writerow(row)

    def getEmployeeHeaders(self):
        with open(self.FILE_NAME, encoding="utf-8-sig") as _file:
            dict_reader = csv.DictReader(_file)            
            return dict_reader.fieldnames