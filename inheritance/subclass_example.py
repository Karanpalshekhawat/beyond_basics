"""
Example of how to use subclasses.

Reuse the already defined classes init variables into other subclasses

isinstance and issubclass are 2 important builtin methods inside python
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

# will show you the structure, first look for details in developer class and then employee and then built-ins
print(help(developer))

"""
Important way of how to use employee init and also create a new init for developer class
"""


class developer_1(employee):

    # only addding new prog lang variable in developer init, will use assigning capabilities from employee init
    def __init__(self, name, last, pay, prog_lang):
        """super will pass whatever arguments you give to our employee class"""
        super().__init__(name, last, pay)
        # same above can be used like employee.__init__(self, name, last, pay)
        self.prog_lang = prog_lang


class Manager(employee):

    def __init__(self, name, last, pay, employees=None):
        """Do not pass mutable objects as default arguments"""
        super().__init__(name, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # emp can be object which is created from the above 2 class
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname)
