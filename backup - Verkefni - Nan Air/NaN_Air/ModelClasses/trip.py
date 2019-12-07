class Trip():

    def __init__(self, tripDict):
        
        self.__destination = tripDict["airportID"]
        self.__depart_Time_Home = tripDict["depart_Time"]
        self.__arrival_Time_Dest = tripDict["arrival_Time_Dest"]
        self.__depart_Time_Abr = tripDict["depart_Time_Abr"]
        self.__arrival_Time_Home = tripDict["arrival_Time_Home"]
 
    def get_destination(self):
        return self.__destination

    def get_depart_Time_Home(self):
        return self.__depart_Time_Home

    def get_arrival_Time_Dest(self):
        return self.__arrival_Time_Dest

    def get_depart_Time_Abr(self):
        return self.__depart_Time_Abr

    def get_arrival_Time_Home(self):
        return self.__arrival_Time_Home
