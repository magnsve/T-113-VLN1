#Planes class

class Planes ():

    def __init__ (self, planeDict):
        self.__insignia = planeDict["plane_insignia"]
        self.__typeID = planeDict["plane_type_ID"]
        self.__manufacturer = planeDict["plane_manufacturer"]
        self.__model = planeDict["plane_model"]
        self.__capacity = planeDict["plane_capacity"]

def main():
    planeDict = {"plane_insignia": "NA020", "plane_type_ID": "NAFokkerF100", "plane_manufacturer": "Fokker", "plane_model": "F100", "plane_capacity": "100"}
    plane = Planes(planeDict)
    print(plane)
    
main()