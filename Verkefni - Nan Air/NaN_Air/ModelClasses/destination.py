# Imports and constants

# Classes
class Destination():
    ''' '''
    def __init__(self, input_data = None):
        self.set_airportId(input_data)
        self.set_destination(input_data)
        self.set_country(input_data)
        self.set_flightTime(input_data)
        self.set_distance(input_data)
        self.set_ice(input_data)
        self.set_iceNumber(input_data)

    def __str__(self):
        output = ''
        for attr in self.__dict__.values():
            output += '{},'.format(attr)
        return output

    def set_iceNumber(self, input_data):
        if not input_data:
            self.__iceNumber = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__iceNumber = input_data['iceNumber']
                except KeyError:
                    self.__iceNumber = ''
            else:
                self.__iceNumber = input_data
    
    def set_ice(self, input_data):
        if not input_data:
            self.__ice = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__ice = input_data['ice']
                except KeyError:
                    self.__ice = ''
            else:
                self.__ice = input_data
    
    def set_distance(self, input_data):
        if not input_data:
            self.__distance = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__distance = input_data['distance']
                except KeyError:
                    self.__distance = ''
            else:
                self.__distance = input_data
    
    def set_flightTime(self, input_data):
        if not input_data:
            self.__flightTime = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__flightTime = input_data['flightTime']
                except KeyError:
                    self.__flightTime = ''
            else:
                self.__flightTime = input_data

    def set_country(self, input_data):
        if not input_data:
            self.__country = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__country = input_data["country"]
                except KeyError:
                    self.__country = ''
            else:
                self.__country = input_data

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

    def set_airportId(self, input_data):
        if not input_data:
            self.__airportId = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__airportId = input_data["airportId"]
                except KeyError:
                    self.__airportId = ''
            else:
                self.__airportId = input_data


    def get_airportId(self):        
        return self.__airportId

    def get_destinations(self):
        return self.__destination
    
    def get_country(self):
        return self.__country

    def get_flightTime(self):
        return self.__flightTime

    def get_distance(self):
        return self.__distance

    def get_ice(self):
        return self.__ice

    def get_iceNumber(self):
        return self.__iceNumber
    
