class employee:

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.last)

    def __repr__(self):
        return "employee({}, {}, {})".format(self.name, self.last, self.pay)
