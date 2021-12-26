""" In python, you can define functions inside functions known as local functions
    can call inside that function
"""


def sort_by_last(string):
    def last(s):
        # local function
        return s[-1]

    return sorted(string, key=last)


print(sort_by_last(['ab', 'aa', 'at', 'ad']))

"""
One important thing is you cannot call local function 
as container_functions.local_function.
Local functions are not members of containing function.
"""


def outer():
    def inner():
        print("local function")

    return inner


lf = outer()

print(lf)
