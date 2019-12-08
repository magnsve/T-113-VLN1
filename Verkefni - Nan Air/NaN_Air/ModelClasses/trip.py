class Trip():

    def __init__(self, input_data = None):
        
        self.set_destination(input_data)
        self.set_plane(input_data)
        self.set_pilot(input_data)
        self.set_cabincrew(input_data)
        self.set_sold_seats(input_data)
        self.set_available_seats(input_data)
        self.set_first_trip(input_data)
        self.set_second_trip(input_data)
        self.set_depart_time_home(input_data)
        self.set_arrival_time_dest(input_data)
        self.set_depart_time_dest(input_data)
        self.set_arrival_time_home(input_data)
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
    
    def set_pilot(self, input_data):
        if not input_data:
            self.__pilot = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__pilot = input_data["pilot"]
                except KeyError:
                    self.__pilot = ''        
            else:
                self.__pilot = input_data

    def set_cabincrew(self, input_data):
        if not input_data:
            self.__cabincrew = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__cabincrew = input_data["cabincrew"]
                except KeyError:
                    self.__cabincrew = ''        
            else:
                self.__cabincrew = input_data

    def set_sold_seats(self, input_data):
        if not input_data:
            self.__sold_seats = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__sold_seats = input_data["sold_seats"]
                except KeyError:
                    self.__sold_seats = ''        
            else:
                self.__sold_seats = input_data

    def set_available_seats(self, input_data):
        if not input_data:
            self.__available_seats = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__available_seats = input_data["available_seats"]
                except KeyError:
                    self.__available_seats = ''        
            else:
                self.__available_seats = input_data

    def set_first_trip(self, input_data):
        if not input_data:
            self.__first_trip = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__first_trip = input_data["first_trip"]
                except KeyError:
                    self.__first_trip = ''        
            else:
                self.__first_trip = input_data
    def set_second_trip(self, input_data):
        if not input_data:
            self.__second_trip = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__second_trip = input_data["second_trip"]
                except KeyError:
                    self.__second_trip = ''        
            else:
                self.__second_trip = input_data

    
    def set_depart_time_home(self, input_data):
        if not input_data:
            self.__depart_time_home = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__depart_time_home = input_data["depart_time_home"]
                except KeyError:
                    self.__depart_time_home = ''
            else:
                self.__depart_Time_Home = input_data
    
    def set_arrival_time_dest(self, input_data):
        if not input_data:
            self.__arrival_time_dest = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__arrival_time_dest = input_data["arrival_time_dest"]
                except KeyError:
                    self.__arrival_time_dest = ''
            else:
                self.__arrival_time_dest = input_data        
    
    def set_depart_time_dest(self, input_data):
        if not input_data:
            self.__depart_time_dest = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__depart_time_dest = input_data["depart_time_dest"]
                except KeyError:
                    self.__depart_time_dest = ''
            else:
                self.__depart_time_dest = input_data   
    
    def set_arrival_time_home(self, input_data):
        if not input_data:
            self.__arrival_time_home = ''
        else:
            if isinstance(input_data, dict):            
                try:
                    self.__arrival_time_home = input_data["arrival_time_home"]
                except KeyError:
                    self.__arrival_time_home = ''
            else:
                self.__arrival_time_home = input_data   
    
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
