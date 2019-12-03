import csv
from logicLayer.employeedata import Employee
 
class Employee:
    dataBase = "prufaverklegt.csv"
    def read_file(self,filepath = dataBase):
        emptylist = []
        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance = Employee(row)
                emptylist.append[instance]
            print(emptylist)
 
    def set_employee(self,filepath,Employee):
        data = Prepare_for_csv()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            return f

class Trip:
    dataBase = "prufaverklegt.csv"
    def read_file(self,filepath = dataBase):
        emptylist = []
        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance = Trip(row)
                emptylist.append[instance]
            print(emptylist)
 
    def set_employee(self,filepath,Trip):
        data = Prepare_for_csv()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            return f

class Plane:
    dataBase = "prufaverklegt.csv"
    def read_file(self,filepath = dataBase):
        emptylist = []
        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance = Plane(row)
                emptylist.append[instance]
            print(emptylist)
 
    def set_employee(self,filepath,Plane):
        data = Prepare_for_csv()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            return f

class Destination:
    dataBase = "prufaverklegt.csv"
    def read_file(self,filepath = dataBase):
        emptylist = []
        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance = Destination(row)
                emptylist.append[instance]
            print(emptylist)
 
    def set_employee(self,filepath,Destination):
        data = Prepare_for_csv()
        with open(filepath,'a') as f:
            writer=csv.writer(f)
            writer.writerow(data)
            return f
