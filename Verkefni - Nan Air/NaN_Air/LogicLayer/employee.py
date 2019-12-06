# Imports and constants

# Classes
class Employee():
    ''' '''
    def __init__(self, employeeDict = {}):
        self.set_ssn(employeeDict)
        self.set_name(employeeDict)
        self.set_role(employeeDict)
        self.set_rank(employeeDict)
        self.set_licence(employeeDict)
        self.set_address(employeeDict)
        self.set_phonenumber(employeeDict)

    def __str__(self):
        return '{},{},{},{},{},{},{}'.format(self.__ssn, self.__name, self.__role, self.__rank, self.__licence, self.__address, self.__phonenumber)

    def get_ssn(self):        
        return self.__ssn

    def get_name(self):
        return self.__name
    
    def get_role(self):
        return self.__role

    def get_rank(self):
        return self.__rank

    def get_licence(self):
        return self.__licence

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber
    
    def set_ssn(self, employeeDict):
        try:
            self.__ssn = employeeDict["ssn"]
        except KeyError:
            self.__ssn = ''
    
    def set_name(self, employeeDict):
        try:
            self.__name = employeeDict["name"]
        except KeyError:
            self.__name = ''
    
    def set_role(self, employeeDict):
        try:
            self.__role = employeeDict["role"]
        except KeyError:
            self.__role = ''
    
    def set_rank(self, employeeDict):
        try:
            self.__rank = employeeDict["rank"]
        except KeyError:
            self.__rank = ''
    
    def set_licence(self, employeeDict):
        try:
            self.__licence = employeeDict["licence"]
        except KeyError:
            self.__licence = ''
    
    def set_address(self, employeeDict):
        try:
            self.__address = employeeDict["address"]
        except KeyError:
            self.__address = ''
    
    def set_phonenumber(self, employeeDict):
        try:
            self.__phonenumber = employeeDict["phonenumber"]
        except KeyError:
            self.__phonenumber = ''