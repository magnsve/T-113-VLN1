#imports and constants
import csv, codecs
from ModelClasses.plane import Plane

#Classes
class DL_Planes():
    ''' This class handles the database for Destinations. It has four methods:
        
        1) getPlanes:         This method reads the database and returns each line as a Plane object.
        2) appendPlanes:      This method appends a Plane object to the bottom of the database.
        3) modifyPlanes:      This method writes over an entry in the database. 
        4) getPlanesHeaders:  This method returns a list with the header row. '''

    FILE_NAME = 'DataLayer\\DL_Database\\Planes.csv'
    ENCODING = 'utf-8'

    def getPlanes(self):
        output = []
        with codecs.open(self.FILE_NAME, 'r', self.ENCODING) as _file:
            reader = csv.reader(_file)
            headers = next(reader)
            for row in reader:
                row_dict = dict(zip(headers,row))
                plane_from_row = Plane(row_dict)
                output.append(plane_from_row)
        return output

    def appendPlanes(self, plane_object):
        with codecs.open(self.FILE_NAME, 'a', self.ENCODING) as _file:
            _file.write(plane_object.__str__())
        return True
    
    def modifyPlanes(self, plane_object, index):
        list_of_planes = self.getPlanes()
        headers = self.getPlanesHeaders()
        with codecs.open(self.FILE_NAME, 'w', self.ENCODING) as _file:
            writer = csv.writer(_file)
            list_of_planes[index] = plane_object
            output = [headers]
            for plane in list_of_planes:
                value_list = plane.__str__().split(',')
                output.append(value_list)
            for row in output:
                writer.writerow(row)

    def getPlanesHeaders(self):
        with open(self.FILE_NAME, encoding="utf-8-sig") as _file:
            dict_reader = csv.DictReader(_file)            
            return dict_reader.fieldnames