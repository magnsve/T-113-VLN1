from DataLayer.dl_api import DL_API

class LL_Employee():

    def changeEmployee():
        pass

    def searchEmployee():
        pass

    def removeEmployee():
        pass

    def inactivateEmployee(self, employee_object, index):
        api_instance = DL_API()
        employee_object.set_status()
        api_instance.modify_employee(employee_object, index)