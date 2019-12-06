#imports and constants
import csv
from LogicLayer.LL_API import LL_API

#Classes

class DL_Destinations():
    ''' '''
    FILE_NAME = 'Destinations.csv'

    def getDestinations(self):
        input_file = csv.DictReader(open(self.FILE_NAME))
        output = []
        for row in input_file:
            data = LL_API.createDestination(row)
            output.append(data)
        return output

    def appendDestinations(self, destination_object):
        
        #append to CSV
        pass

    def modifyDestinations(self, destination_object, index):
        pass