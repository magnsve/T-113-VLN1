from DataLayer.dl_api import DL_API
from ModelClasses.destination import Destination

class LL_Destinations():

    def searchDestination(self, destination_object):
        #okkur vantar fleiri upplýsingar hér
        list_of_destinations = DL_API().get_destinations   
        id_search = self.search_id(destination_object, list_of_destinations)        
        destination_search = self.search_destination(destination_object, id_search)
        status_search = self.search_status(destination_object, destination_search)
        history_search = self.search_history(destination_object, status_search)
        return history_search

    def search_id(self, destination_object, list_of_destinations):
        ID = destination_object.get_id()
        output = []
        if not ID:
            return list_of_destinations
        elif ID != '':
            for destination in list_of_destinations:
                if destination in destination.get_id():
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