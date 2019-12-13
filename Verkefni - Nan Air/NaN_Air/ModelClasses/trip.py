class Trip():

    def __init__(self, input_data = None):        
        self.set_destination(input_data)
        self.set_out_flight_nr(input_data)
        self.set_out_dep(input_data)
        self.set_in_flight_nr(input_data)
        self.set_in_dep(input_data)
        self.set_plane(input_data)
        self.set_capacity(input_data)
        self.set_captain(input_data)
        self.set_copilot(input_data)
        self.set_fsm(input_data)
        self.set_fa1(input_data)
        self.set_fa2(input_data)
        self.set_fa3(input_data)
        self.set_fa4(input_data)
        self.set_fa5(input_data)
        self.set_status(input_data)

    def __str__(self):
        return '{},{},{},{},{},{},{},{},{},{},{},{},'.format(self.__destination, self.__plane, self.__capacity, self.__captain, self.__copilot, self.__fsm, self.__fa1, self.__fa2, self.__fa3, self.__fa4, self.__fa5, self.__status)

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

    def set_plane(self, input_data):
        if not input_data:
            self.__plane = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__plane = input_data["plane"]
                except KeyError:
                    self.__plane = ''        
            else:
                self.__plane = input_data
    
    def set_copilot(self, input_data):
        if not input_data:
            self.__copilot = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__copilot = input_data["copilot"]
                except KeyError:
                    self.__copilot = ''        
            else:
                self.__copilot = input_data

    def set_captain(self, input_data):
        if not input_data:
            self.__captain = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__captain = input_data["captain"]
                except KeyError:
                    self.__captain = ''        
            else:
                self.__captain = input_data

    def set_out_flight_nr(self, input_data):
        if not input_data:
            self.__out_flight_nr = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__out_flight_nr = input_data["out_flight_nr"]
                except KeyError:
                    self.__out_flight_nr = ''        
            else:
                self.__out_flight_nr = input_data

    def set_out_dep(self, input_data):
        if not input_data:
            self.__out_dep = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__out_dep = input_data["out_dep"]
                except KeyError:
                    self.__out_dep = ''        
            else:
                self.__out_dep = input_data

    def set_in_flight_nr(self, input_data):
        if not input_data:
            self.__in_flight_nr = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__in_flight_nr = input_data["in_flight_nr"]
                except KeyError:
                    self.__in_flight_nr = ''        
            else:
                self.__in_flight_nr = input_data
    
    def set_in_dep(self, input_data):
        if not input_data:
            self.__in_dep = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__in_dep = input_data["in_dep"]
                except KeyError:
                    self.__in_dep = ''        
            else:
                self.__in_dep = input_data

    
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
                self.__capacity = input_data
    
    def set_fsm(self, input_data):
        if not input_data:
            self.__fsm = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__fsm = input_data["fsm"]
                except KeyError:
                    self.__fsm = ''
            else:
                self.__fsm = input_data        
    
    def set_fa1(self, input_data):
        if not input_data:
            self.__fa1 = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__fa1 = input_data["fa1"]
                except KeyError:
                    self.__fa1 = ''
            else:
                self.__fa1 = input_data   
    
    def set_fa2(self, input_data):
        if not input_data:
            self.__fa2 = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__fa2 = input_data["fa2"]
                except KeyError:
                    self.__fa2 = ''
            else:
                self.__fa2 = input_data   
    
    def set_fa3(self, input_data):
        if not input_data:
            self.__fa3 = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__fa3 = input_data["fa3"]
                except KeyError:
                    self.__fa3 = ''
            else: 
                self.__fa3 = input_data

    def set_fa4(self, input_data):
        if not input_data:
            self.__fa4 = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__fa4 = input_data["fa4"]
                except KeyError:
                    self.__fa4 = ''
            else:
                self.__fa4 = input_data

    def set_fa5(self, input_data):
        if not input_data:
            self.__fa5 = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__fa5 = input_data["fa5"]
                except KeyError:
                    self.__fa5 = ''
            else:
                self.__fa5 = input_data

    def set_status(self, input_data):
        if not input_data:
            self.__status = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__status = input_data["status"]
                except KeyError:
                    self.__status = ''
            else:
                self.__status = input_data
 
    def get_destination(self):
        return self.__destination
    
    def get_out_flight_nr(self):
        return self.__out_flight_nr

    def get_out_dep(self):
        return self.__out_dep
    
    def get_in_flight_nr(self):
        return self.__in_flight_nr
    
    def get_in_dep(self):
        return self.__in_dep
    
    def get_plane(self):
        return self.__plane
    
    def get_capacity(self):
        return self.__capacity
    
    def get_captain(self):
        return self.__captain
    
    def get_copilot(self):
        return self.__copilot
    
    def get_fsm(self):
        return self.__fsm
    
    def get_fa1(self):
        return self.__fa1
    
    def get_fa2(self):
        return self.__fa2
    
    def get_fa3(self):
        return self.__fa3
    
    def get_fa4(self):
        return self.__fa4
    
    def get_fa5(self):
        return self.__fa5
    
    def get_status(self):
        return self.__status