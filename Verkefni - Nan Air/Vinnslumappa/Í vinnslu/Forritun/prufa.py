import shutil

def get_terminal_columns():
    return shutil.get_terminal_size().columns

import textwrap

def print_autobreak(*text, sep=' '):
    width = get_terminal_columns() - 20
    for line in sep.join(map(str, text)).splitlines(True):
        print(*textwrap.wrap(line, width), sep="\n")

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vitae odio quis felis consectetur blandit. Etiam mattis vehicula ex id sodales. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fermentum semper nisi vel aliquam. Ut nec facilisis lectus. Maecenas auctor blandit condimentum. Donec finibus orci ac imperdiet congue. Pellentesque sem leo, commodo non metus ac, posuere maximus lorem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. "

print_autobreak(text)

#print(text)