#imports and constants
import csv
from ModelClasses.destination import Destination

#Classes

class DL_Destinations():
    ''' '''
<<<<<<< HEAD
    FILE_NAME = "DataLayer\\DL_Database\\Destinations.csv"

=======
    FILE_NAME = 'DataLayer\\Destinations.csv'
>>>>>>> 022489568675c381e1991b104393f13fb3cf42bd

    def getDestinations(self):
        _file = csv.DictReader(open(self.FILE_NAME))
        output = []
        for row in _file:
            data = Destination(row)
            output.append(data)
        return output

    def appendDestinations(self, destination_object):
        with open(self.FILE_NAME, 'a') as _file:
            _file.write("\n")
            _file.write(destination_object.__str__())
        return True        

    def modifyDestinations(self, destination_object, index):
        lines = open(self.FILE_NAME).read().splitlines()
        print(lines)
        print(destination_object.__str__())
        lines[index] = destination_object.__str__()
        open(self.FILE_NAME,'w').write('\n'.join(lines))
        return True
    
    def getHeaders(self):
        with open(self.FILE_NAME) as _file:
            dict_reader = csv.DictReader(_file)
            return dict_reader.fieldnames