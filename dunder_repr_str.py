"""
Always add these 2 special methods inside any class so
that if any more developer works they can retrieve information

repr helps in how the class was instantiated
while
str helps ing giving more information about the instantiated
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

    def __repr__(self):
        return "employee( {}, {}, {} )".format(self.name, self.last, self.pay)

    def __str__(self):
        return ' Name is {} while email is {} '.format(self.name, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = employee('Karan', 'Singh', 1000)
emp2 = employee('Komal', 'Rathore', 2000)

print(emp1.__repr__())
print(repr(emp1))

print(emp1.__str__())
print(str(emp1))

# if adding classes it will look into __add__ method inside the class
# there are many methods for arithmatic
print(emp1 + emp2)

# length function on object, same output in below
print('test_case'.__len__())
print(len('test_case'))

# lenght of fullname

print(len(emp1))
print(len(emp2))
