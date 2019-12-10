from DataLayer.dl_api import DL_API
from LogicLayer.ll_api import LL_API
from ModelClasses.employee import Employee
from ModelClasses.destination import Destination
from InterfaceLayer.il_employee_search_menu import IL_EmployeeSearchMenu


_dict = {'ssn':'2910858778','name':'Virginia Ho','role':'Pilot','rank':'Captain','licence':'NABAE146','address':'Fellsmúli 2','phonenumber':'8998802'}
x = Employee(_dict)
_list = DL_API().get_employees()
for item in _list:
    print(item)


#headers = DL_API().get_employee_headers()
#print(headers)

# DL_API().modify_employee(x,2)