"""
if you are using our arguments of init to set up another variable
like email in the below example then we have to use property decorator

If After assigning class, we have to change one of the variables in init
we can directly do it using the variable from object

But it will not update the email variable which would be same what we
have assigned to it during first instance creation.

One way to solve this is to create a method for email but then everyone
have to use () after their call in the code.

If you don't want everyone to change their codebase just define property
decorator in front the new wmail method as in class employee 2
"""


class employee:

    def __init__(self, name, last):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.name, self.last)


emp_1 = employee('Karan', 'shekhawat')

emp_1.name = "Komal"

print(emp_1.name)
print(emp_1.email)
print(emp_1.fullname())


class employee2:

    def __init__(self, name, last):
        self.name = name
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    # if we want the capability to set up also
    @fullname.setter
    def fullname(self, name):
        name, last = name.split(' ')
        self.name = name
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('deleting name')
        self.name = None
        self.last = None


emp_1 = employee2('Karan', 'shekhawat')

emp_1.name = "Komal"

print(emp_1.name)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'JP Singh'

print(emp_1.name)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.name)
print(emp_1.email)
print(emp_1.fullname)
