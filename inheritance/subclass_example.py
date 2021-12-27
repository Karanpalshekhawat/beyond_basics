"""
Example of how to use subclasses.

Reuse the already defined classes init variables into other subclasses
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


class developer(employee):
    pass


# Can access all the attributes and methods of employee class like this
dev_1 = developer('Karan', 'Singh', 5000)
dev_2 = developer('komal', 'Rathore', 5000)

# will show you the strucutre, first look for details in developer class and then employee and then built-ins
print(help(developer))

"""
Important way of how to use employeee init and also create a new init for developer class
"""

