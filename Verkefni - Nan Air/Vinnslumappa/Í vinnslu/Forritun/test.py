import sys
import shutil


c = '+'
v = '|'
h = '-'
s = ' '

def get_terminal_size():
    return shutil.get_terminal_size()

filestream = open('Header.txt','r')
header = []
for line in filestream:
    header.append(line.strip('\n'))

window_width = get_terminal_size()[0] - 10
window_height = get_terminal_size()[1] - 10
os.system("clear")

for i in range(window_height):
    print()
print(s*5 +c + h*window_width + c)
for line in header:
    print(s*5 +c + line.center(window_width,h) + c)
print(s*5 + c + h * window_width + c)
print(s*5 + v + "Welcome to your NaN Air Managers home page.".center(window_width) + v)
print(s*5 + v+" ".center(window_width)+v)
print(s*5 + v + "To continue, please select an option from the menu.".center(window_width) + v)
print(s*5 + c + h * window_width + c)
print(s*5 + v + s * 5 + "1 - Employee management".ljust(window_width-5) + v)
print(s*5 +v + s * 5 + "2 - Airplane management".ljust(window_width-5) + v)
print(s*5 +v + s * 5 + "3 - Destination management".ljust(window_width-5) + v)
print(s*5 +v + s * 5 + "4 - Trip management".ljust(window_width-5) + v)
for i in range(window_height-20):
    print(s*5 + v + s * window_width + v)
print(s*5 + v + "Type 'Quit' to exit.".rjust(window_width-5) + s * 5 + v)
print(s*5 + c + h * window_width + c)

# inputa = input(" "*32 + "Your choice: ")


