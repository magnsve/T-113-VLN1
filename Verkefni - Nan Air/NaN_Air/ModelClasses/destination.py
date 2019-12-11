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

    def set_emergencyContactNumber(self, input_data):
        if not input_data:
            self.__emergencyContactNumber = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__emergencyContactNumber = input_data['emergencyContactNumber']
                except KeyError:
                    self.__emergencyContactNumber = ''
            else:
                self.__emergencyContactNumber = input_data
    
    def set_emergencyContact(self, input_data):
        if not input_data:
            self.__emergencyContact = ''
        else:
            if isinstance(input_data, dict):
                try:
                    self.__emergencyContact = input_data['emergencyContact']
                except KeyError:
                    self.__emergencyContact = ''
            else:
                self.__emergencyContact = input_data
    
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

    def get_emergencyContact(self):
        return self.__emergencyContact

    def get_emergencyContactNumber(self):
        return self.__emergencyContactNumber
    
    def get_status(self):
        return self.__status
    
    def get_history(self):
        return self.__history