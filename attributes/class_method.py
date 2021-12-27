"""
Class method decorator,
function that we use everytime we instantiate class.

Tp update class variables in all the instances of class.
"""


class shipingcontainers:
    next_serial = 1445

    @classmethod
    def _get_next_serial(cls):
        # variable that we are using is class variables
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, own, cont):
        self.own = own
        self.cont = cont
        self.serial = shipingcontainers._get_next_serial()


c1 = shipingcontainers("YML", "books")
c2 = shipingcontainers("true", "story")

print(shipingcontainers.next_serial)
# value rite now of the class attribute
print(c1.next_serial)
print(c2.next_serial)
