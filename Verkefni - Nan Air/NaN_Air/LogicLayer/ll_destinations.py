from DataLayer.dl_api import DL_API
from ModelClasses.destination import Destination

class LL_Destinations():
    ''' This Class handles the logic for Destinations. It has 5 main methods and a number of minor methods.
        The difference is that the minor methods are only used within one of the main methods.
        The main methods are:
        1)  searcDestination: This method takes in an Destination object and uses it's attributes to narrow down the 
            database. It then returns the resulting list of objects. This method uses the minor methods to search 
            for each attribute.
        
        2)  get_destination_file_headers: This method calls the DL_API directly to fetch the database column names.
        
        3)  find_index_in_database: This method compares a Destination object to the database, using the __str__ overload.
            If it returns a match it gives the index number in the database, otherwise it returns None.
        
        4)  edit_destination_object: This method calls to the DL_API to replace an object in the database.

        5)  add_destination: This method calls to the DL_API to append an object to the database. '''
    
    def search_destination(self, destination_object):        
        list_of_destinations = DL_API().get_destinations()
        airportId_search = self.search_airportId(destination_object, list_of_destinations)        
        destination_search = self.searchDestination(destination_object, airportId_search)
        country_search = self.search_country(destination_object, destination_search)
        flightTime = self.search_flightTime(destination_object, country_search)
        distance_search = self.search_distance(destination_object, flightTime)
        ice_search = self.search_ice(destination_object, distance_search)
        iceNumber_search = self.search_iceNumber(destination_object, ice_search)
        return iceNumber_search

    def search_airportId(self, destination_object, list_of_destinations):
        airportId = destination_object.get_airport_id()
        output = []
        if not airportId:
            return list_of_destinations
        elif airportId != '':
            for destination in list_of_destinations:
                if destination.lower() in destination.get_airportId().lower():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_country(self, destination_object, list_of_destinations):
        country = destination_object.get_country()
        output = []
        if not country:
            return list_of_destinations
        elif country != '':
            for destination in list_of_destinations:
                if destination.lower() in destination.get_country().lower():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_flightTime(self, destination_object, list_of_destinations):
        flightTime = destination_object.get_flight_time()
        output = []
        if not flightTime:
            return list_of_destinations
        elif flightTime != '':
            for destination in list_of_destinations:
                if destination.lower() in destination.get_flightTime().lower():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def searchDestination(self, destination_object, list_of_destinations):
        destination = destination_object.get_destinations()
        output = []
        if not destination:
            return list_of_destinations
        elif destination != '':
            for destinations in list_of_destinations:
                if destinations.lower() in destination.get_destinations().lower():
                    output.append(destinations)
            return output
        else:
            return list_of_destinations

    def search_distance(self, destination_object, list_of_destinations):
        distance = destination_object.get_distance()
        output = []
        if not distance:
            return list_of_destinations
        elif distance != '':
            for destinations in list_of_destinations:
                if destinations.lower() in destinations.get_distance().lower():
                    output.append(destinations)
            return output
        else:
            return list_of_destinations

    def search_ice(self, destination_object, list_of_destinations):
        ice = destination_object.get_ice()
        output = []
        if not ice:
            return list_of_destinations
        elif ice != '':
            for destination in list_of_destinations:
                if destination.lower() in destination.get_ice().lower():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_iceNumber(self, destination_object, list_of_destinations):
        iceNumber = destination_object.get_ice_number()
        output = []
        if not iceNumber:
            return list_of_destinations
        elif iceNumber != '':
            for destination in list_of_destinations:
                if destination.lower() in destination.get_ice_number().lower():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def get_destination_file_headers(self):
        return DL_API().get_destinations_headers()

    def find_index_in_database(self, destination_object):        
        list_of_destinations = DL_API().get_destinations()
        for index, destination in enumerate(list_of_destinations):
            if destination.__str__() == destination_object.__str__():
                return index
        return None
    
    def edit_destination_object(self, destination_object, index):
        return DL_API().modify_destinations(destination_object, index)
        
    def add_destination(self, destination_object):
        return DL_API().append_destinations(destination_object)
    
    def ll_set_airport_id(self, destination_object, input_data):
        return destination_object.set_airport_id(input_data)
    
    def ll_set_destination(self, destination_object, input_data):
        return destination_object.set_destination(input_data)
    
    def ll_set_distance(self, destination_object, input_data):
        return destination_object.set_distance(input_data)

    def ll_set_flight_time(self,destination_object, input_data):
        return destination_object.set_flight_time(input_data)

    def ll_set_country(self, destination_object, input_data):
        return destination_object.set_country(input_data)
        
    def ll_set_ice(self, destination_object, input_data):
        return destination_object.set_ice(input_data)
        
    def ll_set_ice_number(self, destination_object, input_data):
        return destination_object.set_ice_number(input_data)
