"""
Suppose you have a class and you want to declare a variable
which you will use and is same in all the instances.

instance attributes are assigned using __init__ method which can
be different for each instances.

Attributes associated with class are class attributes,
these class attributes can be updated permanently inside
the __init__ method
"""


class Shipingcontainers:

    def __init__(self, own, cont):
        self.own = own
        self.cont = cont


c1 = Shipingcontainers("YML", "books")
c2 = Shipingcontainers("true", "story")

# instance attributes
print(c1.own, c1.cont)
print(c2.own, c2.cont)


class Shipingcontainers_class:
    next_serial = 1440

    def __init__(self, own, cont):
        self.own = own
        self.cont = cont
        self.serial = Shipingcontainers_class.next_serial
        Shipingcontainers_class.next_serial += 1


c1 = Shipingcontainers_class("YML", "books")
c2 = Shipingcontainers_class("true", "story")

print(Shipingcontainers_class.next_serial)
# value rite now of the class attribute
print(c1.next_serial)
print(c2.next_serial)
