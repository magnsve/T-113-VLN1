class Plane():

    def __init__ (self, input_data = None):
        self.set_insignia(input_data)
        self.set_typeID(input_data)
        self.set_manufacturer(input_data)
        self.set_model(input_data)
        self.set_capacity(input_data)
        self.set_status(input_data)
        self.set_history(input_data)

    def set_insignia(self, input_data):
        if not input_data:
            self.__insignia = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__insignia = input_data["insignia"]
                except KeyError:
                    self.__insignia = ''        
            else:
                self.__insignia = input_data
    
    def set_typeID(self, input_data):
        if not input_data:
            self.__typeIDe = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__typeID = input_data["typeID"]
                except KeyError:
                    self.__typeID = ''
            else:
                self.__typeID = input_data
    
    def set_manufacturer(self, input_data):
        if not input_data:
            self.__manufacturer = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__manufacturer = input_data["manufacturer"]
                except KeyError:
                    self.__manufacturer = ''
            else:
                self.__manufacturer = input_data        
    
    def set_model(self, input_data):
        if not input_data:
            self.__model = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__model = input_data["model"]
                except KeyError:
                    self.__model = ''
            else:
                self.__model = input_data   
    
    def set_capacity(self, input_data):
        if not input_data:
            self.__capacity = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__capacity = input_data["capacity"]
                except KeyError:
                    self.__capacity = ''
            else:
                self.__licence = input_data   

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


    def get_insignia(self):
        return self.__insignia

    def get_typeID(self):
        return self.__typeID

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity