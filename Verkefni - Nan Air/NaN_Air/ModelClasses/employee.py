# Imports and constants

# Classes
class Employee():
    ''' '''
    def __init__(self, input_data = None):
        self.set_ssn(input_data)
        self.set_name(input_data)
        self.set_role(input_data)
        self.set_rank(input_data)
        self.set_licence(input_data)
        self.set_address(input_data)
        self.set_phonenumber(input_data)
        self.set_status(input_data)
        self.set_history(input_data)
    
    def set_ssn(self, input_data):
        if not input_data:
            self.__ssn = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__ssn = input_data["ssn"]
                except KeyError:
                    self.__ssn = ''        
            else:
                self.__ssn = input_data
    
    def set_name(self, input_data):
        if not input_data:
            self.__name = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__name = input_data["name"]
                except KeyError:
                    self.__name = ''
            else:
                self.__name = input_data
    
    def set_role(self, input_data):
        if not input_data:
            self.__role = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__role = input_data["role"]
                except KeyError:
                    self.__role = ''
            else:
                self.__role = input_data        
    
    def set_rank(self, input_data):
        if not input_data:
            self.__rank = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__rank = input_data["rank"]
                except KeyError:
                    self.__rank = ''
            else:
                self.__rank = input_data   
    
    def set_licence(self, input_data):
        if not input_data:
            self.__licence = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__licence = input_data["licence"]
                except KeyError:
                    self.__licence = ''
            else:
                self.__licence = input_data   
    
    def set_address(self, input_data):
        if not input_data:
            self.__address = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__address = input_data["address"]
                except KeyError:
                    self.__address = ''
            else:
                self.__address = input_data
    
    def set_phonenumber(self, input_data):
        if not input_data:
            self.__phonenumber = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__phonenumber = input_data["phonenumber"]
                except KeyError:
                    self.__phonenumber = ''
            else:
                self.__phonenumber = input_data
    
    def set_status(self, input_data):
        if not input_data:
            self.__status = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__status = input_data["status"]
                except KeyError:
                    self.__status = 'incomplete'
            else: 
                self.__status = input_data

    def set_history(self, input_data):
        if not input_data:
            self.__history = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__history = input_data["history"]
                except KeyError:
                    self.__history = ''
            else:
                self.__history = input_data

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.__ssn, self.__name, self.__role, self.__rank, self.__licence, self.__address, self.__phonenumber, self.__status)

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
    
    def get_status(self):
        return self.__status
    
    def get_history(self):
        return self.__history