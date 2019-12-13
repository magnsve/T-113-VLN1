# Imports and constants

# Classes
class Employee():
    ''' '''
    def __init__(self, input_data = None):        
        self.set_name(input_data)
        self.set_ssn(input_data)
        self.set_role(input_data)
        self.set_rank(input_data)
        self.set_licence(input_data)
        self.set_address(input_data)
        self.set_phonenumber(input_data)
        self.set_gsm(input_data)
        self.set_e_mail(input_data)
    
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
    
    def set_gsm(self, input_data):
        if not input_data:
            self.__gsm = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__gsm = input_data["gsm"]
                except KeyError:
                    self.__gsm = ''
            else:
                self.__gsm = input_data

    def set_e_mail(self, input_data):
        if not input_data:
            self.__e_mail = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__e_mail = input_data["e-mail"]
                except KeyError:
                    self.__e_mail = ''
            else:
                self.__e_mail = input_data

    def __str__(self):
        output = ''
        for attr in self.__dict__.values():
            output += '{},'.format(attr)
        return output

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

    def get_gsm(self):
        return self.__gsm
    
    def get_e_mail(self):
        return self.__e_mail