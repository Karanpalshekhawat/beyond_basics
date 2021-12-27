"""
Example of using class method as an alternative constructor

Sometimes when you have arguments for class in the different format
as you requires, you can use classmethod constructor
"""


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


# initialise new emp using above

emp1 = employee('Karan', 'Singh', 1000)
emp2 = employee('Komal', 'Rathore', 2000)

# Suppose our inputs was in a little different format
emp3 = 'John-Mac-3000'
emp4 = 'Marc-willing-4000'


# We can use class method as constructor like below

class employee2(employee):
    raise_amt = 1.04

    @classmethod
    def from_string(cls, emp_info_str):
        name, last, pay = emp_info_str.split('-')
        return cls(name, last, pay)


new_emp3 = employee2.from_string(emp3)
new_emp4 = employee2.from_string(emp4)

print(new_emp3.email)
print(new_emp4.email)
