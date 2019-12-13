# Imports and constants
from DataLayer.dl_api import DL_API
import string

# Classes
class LL_Employee():
    ''' This Class handles the logic for employees. It has 5 main methods and a number of minor methods.
        The difference is that the minor methods are only used within one of the main methods.
        The main methods are:
        1)  searchEmployee: This method takes in an Employee object and uses it's attributes to narrow down the 
            database. It then returns the resulting list of objects. This method uses the minor methods to search 
            for each attribute.
        
        2)  get_employee_file_headers: This method calls the DL_API directly to fetch the database column names.
        
        3)  find_index_in_database: This method compares an Employee object to the database, using the __str__ overload.
            If it returns a match it gives the index number in the database, otherwise it returns None.
        
        4)  edit_employee_object: This method calls to the DL_API to replace an object in the database.

        5)  add_employee: This method calls to the DL_API to append an object to the database. '''

    def searchEmployee(self, employee_object):        
        list_of_employees = DL_API().get_employees()
        ssn_search = self.search_ssn(employee_object, list_of_employees)        
        name_search = self.search_name(employee_object, ssn_search)
        role_search = self.search_role(employee_object, name_search)
        rank_search = self.search_rank(employee_object, role_search)
        license_search = self.search_licence(employee_object, rank_search)
        address_search = self.search_address(employee_object, license_search)
        phonenumber_search = self.search_phonenumber(employee_object, address_search)

        return phonenumber_search

    def search_phonenumber(self, employee_object, list_of_employees):
        phonenumber = employee_object.get_phonenumber()
        output = []
        if not phonenumber:
            return list_of_employees
        elif phonenumber != '':
            for employee in list_of_employees:
                if phonenumber.lower() in employee.get_phonenumber().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees

    def search_address(self, employee_object, list_of_employees):
        address = employee_object.get_address()
        output = []
        if not address:
            return list_of_employees
        elif address != '':
            for employee in list_of_employees:
                if address.lower() in employee.get_address().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees
    
    def search_licence(self, employee_object, list_of_employees):
        _license = employee_object.get_licence()
        output = []
        if not _license:
            return list_of_employees
        elif _license != '':
            for employee in list_of_employees:
                if _license.lower() in employee.get_licence().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees
    
    def search_rank(self, employee_object, list_of_employees):
        rank = employee_object.get_rank()
        output = []
        if not rank:
            return list_of_employees
        elif rank != '':
            for employee in list_of_employees:
                if rank.lower() in employee.get_rank().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees

    def search_role(self, employee_object, list_of_employees):
        role = employee_object.get_role()
        output = []
        if not role:
            return list_of_employees
        elif role != '':
            for employee in list_of_employees:
                if role.lower() in employee.get_role().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees

    def search_name(self, employee_object, list_of_employees):
        name = employee_object.get_name()
        output = []
        if not name:
            return list_of_employees
        elif name != '':
            for employee in list_of_employees:
                if name.lower() in employee.get_name().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees            
    
    def search_ssn(self, employee_object, list_of_employees):
        ssn = employee_object.get_ssn()
        output = []
        if not ssn:
            return list_of_employees
        elif ssn != '':
            for employee in list_of_employees:
                if ssn.lower() in employee.get_ssn().lower():
                    output.append(employee)
            return output
        else:
            return list_of_employees

    def get_employee_file_headers(self):
        return DL_API().get_employee_headers()

    def find_index_in_database(self, employee_object):        
        list_of_employees = DL_API().get_employees()
        for index, employee in enumerate(list_of_employees):
            if employee.__str__() == employee_object.__str__():
                return index
        return None
    
    def edit_employee_object(self, employeeEditObject, index):               
        return DL_API().modify_employee(employeeEditObject, index)
        
    def add_employee(self, employee_object):
        return DL_API().append_employee(employee_object)

    def ll_set_ssn(self, employee_object, input_data):
        list_of_employees = DL_API().get_employees()
        valid = True
        for employee in list_of_employees:
            if employee.get_ssn() == input_data:
                valid = False
                break
        if valid:            
            if employee_object.get_ssn() == '':
                ssn = ''
                for char in input_data:                
                    if char in string.punctuation or char == ' ':
                        pass
                    else:
                        ssn += char
                if len(ssn) == 10:
                    return employee_object.set_ssn(ssn)
                else:
                    return 'Invalid SSN, please try again.'
            else:
                return 'This employee already has an SSN.'
        else:
            return 'This SSN is already in use.'

    def ll_set_name(self, employee_object, input_data):        
        if employee_object.get_name() == '':
            return employee_object.set_name(input_data)
        else:
            return 'This employee already has a name.'
    
    def ll_set_role(self, employee_object, input_data):
        return employee_object.set_role(input_data)
    
    def ll_set_rank(self, employe_object, input_data):
        return employe_object.set_rank(input_data)
    
    def ll_set_licence(self, employee_object, input_data):
        return employee_object.set_licence(input_data)
    
    def ll_set_address(self, employee_object, input_data):
        return employee_object.set_address(input_data)
    
    def ll_set_phonenumber(self, employee_object, input_data):
        return employee_object.set_phonenumber(input_data)
    
    def ll_set_gsm(self, employee_object, input_data):
        return employee_object.set_gsm(input_data)
    
    def ll_set_e_mail(self, employee_object, input_data):
        if '@' in input_data:
            return employee_object.set_e_mail(input_data)
        else:
            return 'Invalid e-mail, please try again.'