""" Test how to use __call__"""





"""
parameters you pass in Init is used to start a class or instantiate a class
while parameters you pass in 
"""

import socket

class Resolver():

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache


class Wages():

    def __init__(self, hour_wage):
        self.wage = hour_wage

    def __call__(self, hour_work):
        total_wage = self.wage * hour_work
        return total_wage

"""
A way to call the Wages class

wg = Wages(hourly wage)
total_wage = wg(10)
If number of working hours is same but hourly wage is different
"""