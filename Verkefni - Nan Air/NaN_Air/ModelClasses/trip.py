class Trip():

    def __init__(self, input_data = None):
        
        self.set_destination(input_data)
        self.set_depart_Time_Home(input_data)
        self.set_arrival_Time_Dest(input_data)
        self.set_depart_Time_Abr(input_data)
        self.set_arrival_Time_Home(input_data)
        self.set_status(input_data)
        self.set_history(input_data)

    def set_destination(self, input_data):
        if not input_data:
            self.__destination = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__destination = input_data["destination"]
                except KeyError:
                    self.__destination = ''        
            else:
                self.__destination = input_data
    
    def set_depart_Time_Home(self, input_data):
        if not input_data:
            self.__depart_Time_Home = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__depart_Time_Home = input_data["depart_Time_Home"]
                except KeyError:
                    self.__depart_Time_Home = ''
            else:
                self.__depart_Time_Home = input_data
    
    def set_arrival_Time_Dest(self, input_data):
        if not input_data:
            self.__arrival_Time_Dest = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__arrival_Time_Dest = input_data["arrival_Time_Dest"]
                except KeyError:
                    self.__arrival_Time_Dest = ''
            else:
                self.__arrival_Time_Dest = input_data        
    
    def set_depart_Time_Abr(self, input_data):
        if not input_data:
            self.__depart_Time_Abr = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__depart_Time_Abr = input_data["depart_Time_Abr"]
                except KeyError:
                    self.__depart_Time_Abr = ''
            else:
                self.__depart_Time_Abr = input_data   
    
    def set_arrival_Time_Home(self, input_data):
        if not input_data:
            self.__arrival_Time_Home = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__arrival_Time_Home = input_data["arrival_Time_Home"]
                except KeyError:
                    self.__arrival_Time_Home = ''
            else:
                self.__arrival_Time_Home = input_data   
    
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

 
    def get_destination(self):
        return self.__destination

    def get_depart_Time_Home(self):
        return self.__depart_Time_Home

    def get_arrival_Time_Dest(self):
        return self.__arrival_Time_Dest

    def get_depart_Time_Abr(self):
        return self.__depart_Time_Abr

    def get_arrival_Time_Home(self):
        return self.__arrival_Time_Home
