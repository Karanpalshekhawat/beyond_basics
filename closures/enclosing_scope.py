"""
local func uses variable x of the main functions
asnd also remember it for future uses once the call is done
DUE TO CLOSURE

x is kept alive so that if local functin is executed, it can still be use
"""

def outer():

    x = 3

    def inner(y):
        return x + y
    return inner

lf = outer()

print(lf(10))


print(lf.__closure__)

"""
Function factories are thos where we return funciton

used in the cases where we have one main argumnet applied to multiple call to inner

and that main argument can also be changed
"""

def raise_to(exp):
    def power(x):
        return pow(x, exp)
    return power

square = raise_to(2)
cube = raise_to(3)

print(square.__closure__)
print(cube.__closure__)


print(square(5))

print(cube(3))
