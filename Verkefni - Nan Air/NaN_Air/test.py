from DataLayer.dl_api import DL_API
from LogicLayer.ll_api import LL_API

# test
my_dict = {"ssn": "æaskfja"}
LL_API = LL_API()
employee = LL_API.createEmployee(my_dict)
print(employee)
print(employee.get_ssn())

DL_API = DL_API()
employees = DL_API.get_employees()
for element in employees:
    print(element)

DL_API.append_employee(employee)
employees = DL_API.get_employees()
for element in employees:
    print(element)

DL_API.modify_employee(employee,4)
employee = DL_API.get_employees()
for element in employees:
    print(element)