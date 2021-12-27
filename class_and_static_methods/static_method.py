"""
Inheritance example with static method

Static method generally don't take any instance or class variables in use (no use of self or cls in it)

Static method don't pass any thing

It behaves just like regular function but we include them in classes because they have some logical
connections within the class
"""

import datetime


class employee:
    raise_amt = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    def raised_salary(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def from_string(cls, emp_info_str):
        name, last, pay = emp_info_str.split('-')
        return cls(name, last, pay)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = employee('Karan', 'Singh', 1000)
emp2 = employee('Komal', 'Rathore', 2000)

date = datetime.date(2021, 10, 11)

print(employee.isworkday(date))
