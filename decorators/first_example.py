"""
Replace, Modify or enhance functions without changing their definitions

Take callable and return callable

First compile the main function as an object
which as passed as an object to the decorator function

"""
# converts to ascii

def ascii_decorator(f):
    """ Same funcitnality to multiple functions"""
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return ascii_decorator



@ascii_decorator
def vegetable():
    return 'blomkal'

@ascii_decorator
def animal():
    return 'bjorn'

@ascii_decorator
def mineral():
    return 'stal'
