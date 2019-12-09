from DataLayer.dl_api import DL_API
from ModelClasses.destination import Destination

class LL_Destinations():
    ''' Destinations holds methods to be called upon by the interface layer. '''
    
    def searchDestination(self, destination_object):
        #okkur vantar fleiri upplýsingar hér 
        list_of_destinations = DL_API().get_destinations
        airportId_search = self.search_airportId(destination_object, list_of_destinations)        
        destination_search = self.search_destination(destination_object, airportId_search)
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



    def search_destination(self, destination_object, list_of_destinations):
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

    def inactivateDestination(self, destination_object, index):
        destination_object.set_status('inactive')        
        DL_API().modify_destinations(destination_object, index)
    
    def changeDestination():
        pass

    def searchDestination():
        pass

    def removeDestination():
        pass