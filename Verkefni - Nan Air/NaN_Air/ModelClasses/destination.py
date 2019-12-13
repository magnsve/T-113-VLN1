# Imports and constants

# Classes
class Destination():
    ''' '''
    def __init__(self, input_data = None):
        self.set_airport_id(input_data)
        self.set_destination(input_data)
        self.set_country(input_data)
        self.set_flight_time(input_data)
        self.set_distance(input_data)
        self.set_ice(input_data)
        self.set_ice_number(input_data)

    def __str__(self):
        output = ''
        for attr in self.__dict__.values():
            output += '{},'.format(attr)
        return output

    def set_ice_number(self, input_data):
        if not input_data:
            self.__ice_number = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__ice_number = input_data['ice number']
                except KeyError:
                    self.__ice_number = ''
            else:
                self.__ice_number = input_data
    
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
    
    def set_flight_time(self, input_data):
        if not input_data:
            self.__flight_time = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__flight_time = input_data['flight time']
                except KeyError:
                    self.__flight_time = ''
            else:
                self.__flight_time = input_data

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

    def set_airport_id(self, input_data):
        if not input_data:
            self.__airport_id = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__airport_id = input_data["airport id"]
                except KeyError:
                    self.__airport_id = ''
            else:
                self.__airport_id = input_data


    def get_airport_id(self):        
        return self.__airport_id

    def get_destinations(self):
        return self.__destination
    
    def get_country(self):
        return self.__country

    def get_flight_time(self):
        return self.__flight_time

    def get_distance(self):
        return self.__distance

    def get_ice(self):
        return self.__ice

    def get_ice_number(self):
        return self.__ice_number
    
