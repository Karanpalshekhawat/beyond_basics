"""
Class objects are also callable
so they can also be use as a decorator

One of the very important practice for it
to have a __call__ method inside the class
because decrators take a callable and return a callable


Below is an example of a class decorator that counts how many times a functions is called
"""


class call_count:

    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@call_count
def hello(name):
    print("name is {}".format(name))


hello("karan")
hello("komal")
hello("Jap")
hello("kevin")

print(hello.count)

"""Different way of assigning a variable to object class, and then using that as an decorator"""


class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):

        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
                return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

print(rotate_list([1,2,3]))
print(rotate_list([4,5,6]))
