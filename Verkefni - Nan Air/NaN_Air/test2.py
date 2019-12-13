# Imports and constants
import os, sys, string
from InterfaceLayer.il_main_menu import IL_MainMenu
from LogicLayer.ll_api import LL_API
from ModelClasses.destination import Destination
from ModelClasses.employee import Employee
from ModelClasses.plane import Plane
from ModelClasses.trip import Trip

a = '100583-5779'
b = '10 05 83 57 79'
c = ''
for i in b:
    print(i)
    if i in string.punctuation or i == ' ':
        print('here')
        i = ''
    else:
        c += i
print(a)
print(b)
print(c)