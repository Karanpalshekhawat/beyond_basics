def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


t = (11, 12, 1, 3, 14)

print(print_args(*t))

"""
Output will be 
11
12
(1, 3, 14)
"""


def color(red, green, blue, **kwargs):
    print(red)
    print(green)
    print(blue)
    print(kwargs)


colours = {'red': 45, 'green': 56, 'blue': 67, 'alpha': 78, 'what': 100}

color(**colours)
