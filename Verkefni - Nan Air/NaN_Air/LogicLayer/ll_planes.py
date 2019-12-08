from DataLayer.dl_api import DL_API
from ModelClasses.plane import Plane

class LL_Planes():

    def changePlane(self):
        pass
    #nafn, tegund, framleiðandi og fjöldi farþegasæta.
    def searchPlane(self, plane_object):
        list_of_planes = DL_API().get_planes    
        name_search = self.search_name(plane_object, list_of_planes)        
        type_search = self.search_type(plane_object, name_search)
        manufacturer_search = self.search_manudacturer(plane_object, type_search)
        no_seats_search = self.search_no_seats(plane_object, manufacturer_search)
        status_search = self.search_status(plane_object, no_seats_search)
        history_search = self.search_history(plane_object, status_search)
        return history_search

    def search_name(self, plane_object, list_of_planes):
        name = planes_object.get_name()
        output = []
        if not name:
            return list_of_planes
        elif name != '':
            for plane in list_of_planes:
                if name in planes.get_name():
                    output.append(plane)
            return output
        else:
            return list_of_planes


    def search_type(self, plane_object, list_of_planes):
        Type = planes_object.get_type()
        output = []
        if not Type:
            return list_of_planes
        elif Type != '':
            for plane in list_of_planes:
                if Type in planes.get_type():
                    output.append(plane)
            return output
        else:
            return list_of_planes
    
    def search_no_seats(self, plane_object, list_of_planes):
        no_seats = planes_object.get_no_seats()
        output = []
        if not no_seats:
            return list_of_planes
        elif no_seats != '':
            for plane in list_of_planes:
                if no_seats in planes.get_no_seats():
                    output.append(plane)
            return output
        else:
            return list_of_planes



    def search_manufacturer(self, plane_object, list_of_planes):
        manufacturer = planes_object.get_manufacturer()
        output = []
        if not manufacturer:
            return list_of_planes
        elif manufacturer != '':
            for plane in list_of_planes:
                if manufacturer in planes.get_type():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def search_history(self, plane_object, list_of_planes):
        history = planes_object.get_history()
        output = []
        if not history:
            return list_of_planes
        elif history != '':
            for plane in list_of_planes:
                if history in planes.get_history():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def search_status(self, plane_object, list_of_planes):
        status = plane_object.get_status()
        output = []
        if not status:
            return list_of_planes
        elif status != '':
            for plane in list_of_planes:
                if status in plane.get_status():
                    output.append(plane)
            return output
        else:
            return list_of_planes

    def inactivatePlane(self, plane_object, index):
        plane_object.set_status('inactive')        
        DL_API().modify_planes(plane_object, index)
    
    def removePlane(self):
        pass

    def changeEmployee():
        pass
