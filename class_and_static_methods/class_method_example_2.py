"""Class method will change the class variable in all the instances of class """

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
    def set_raised_amt(cls, amt):
        cls.raise_amt = amt


emp1 = employee('Karan', 'Singh', 1000)
emp2 = employee('Komal', 'Rathore', 2000)

print(emp1.raise_amt)
print(emp2.raise_amt)

employee.set_raised_amt(1.15)

print(emp1.raise_amt)
print(emp2.raise_amt)
