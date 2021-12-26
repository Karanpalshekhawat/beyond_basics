"""
Callable return by the decorator 1
is passed to decorator 2 and so on
"""


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


def upper_case(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.upper()

    return wrap


@tracer
@upper_case
def string_map(name):
    return name
