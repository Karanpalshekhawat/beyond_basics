"""
Duck Typing and Easier to ask for forgiveness than permission

Not Duck types means it is Non-Pythonic

Duck Object : Don't care what type of object we are working,
              just care if it can do what kind of thing that
              we want it to do

Just remember if we can replace the If condition with
try and except block then it is more pythonic way (EFTP) (More readable)

Permission here means checking if condition multiple times,
calling object again and again (memory inefficient)

Try to do it and raise condition if error
"""


class Duck:

    def quack(self):
        print('Quack ! Quack')

    def fly(self):
        print('Flap ! Flap')


class Person:

    def quack(self):
        print('I am quacking like a duck')

    def fly(self):
        print('I am flapping my arms')


def quak_and_fly(object):
    if isinstance(object, Duck):
        object.quack()
        object.fly()
    else:
        print("It has to be duck")


"""Duck typing : only care what it do when we ask"""


def not_care_only_care_what_it_do(thing):
    thing.quack()
    thing.fly()


"""Non Pythonic way to check attributes and call it"""


def checking_attributes(obj):
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            obj.quack()
    if hasattr(obj, 'fly'):
        if callable(obj.fly):
            obj.fly()


""" Pythonic way to execute nd call it"""


def checking_attributes_pythonic_way(obj):
    try:
        obj.quack()
        obj.fly()
        obj.check()
    except AttributeError as e:
        print(e)


d = Duck()
quak_and_fly(d)

p = Person()
quak_and_fly(p)

not_care_only_care_what_it_do(d)
not_care_only_care_what_it_do(p)

checking_attributes(d)
checking_attributes(p)

checking_attributes_pythonic_way(d)
checking_attributes_pythonic_way(p)