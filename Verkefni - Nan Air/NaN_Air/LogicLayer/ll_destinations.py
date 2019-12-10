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
        emergencyContact_search = self.search_emergencyContact(destination_object, distance_search)
        emergencyContactNumber_search = self.search_emergencyContactNumber(destination_object, emergencyContact_search)
        status_search = self.search_status(destination_object, emergencyContactNumber_search)
        history_search = self.search_history(destination_object, status_search)
        return history_search

    def search_airportId(self, destination_object, list_of_destinations):
        airportId = destination_object.get_airportId()
        output = []
        if not airportId:
            return list_of_destinations
        elif airportId != '':
            for destination in list_of_destinations:
                if destination in destination.get_airportId():
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
                if destination in destination.get_country():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_flightTime(self, destination_object, list_of_destinations):
        flightTime = destination_object.get_flightTime()
        output = []
        if not flightTime:
            return list_of_destinations
        elif flightTime != '':
            for destination in list_of_destinations:
                if destination in destination.get_flightTime():
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
                if destinations in destination.get_destinations():
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
                if destinations in destinations.get_distance():
                    output.append(destinations)
            return output
        else:
            return list_of_destinations

    def search_emergencyContact(self, destination_object, list_of_destinations):
        emergencyContact = destination_object.get_emergencyContact()
        output = []
        if not emergencyContact:
            return list_of_destinations
        elif emergencyContact != '':
            for destination in list_of_destinations:
                if destination in destination.get_emergencyContact():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_emergencyContactNumber(self, destination_object, list_of_destinations):
        emergencyContactNumber = destination_object.get_emergencyContactNumber()
        output = []
        if not emergencyContactNumber:
            return list_of_destinations
        elif emergencyContactNumber != '':
            for destination in list_of_destinations:
                if destination in destination.get_emergencyContactNumber():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_history(self, destination_object, list_of_destinations):
        history = destination_object.get_history()
        output = []
        if not history:
            return list_of_destinations
        elif history != '':
            for destination in list_of_destinations:
                if history in destination.get_history():
                    output.append(destination)
            return output
        else:
            return list_of_destinations

    def search_status(self, destination_object, list_of_destinations):
        status = destination_object.get_status()
        output = []
        if not status:
            return list_of_destinations
        elif status != '':
            for destination in list_of_destinations:
                if status in destination.get_status():
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