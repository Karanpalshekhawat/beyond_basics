"""
Used in situations where we want values in the tuble
to be named so that it can be identified by anyone easily

Also you cannot use it you want your variables to be immuatable
"""

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(50, 200, 150)
print(color.red)

# this will throw an error as it is immuatable
try:
    color.red = 60
except AttributeError:
    print("Cannot assign anything to immuatable object")
