def check_non_index(index):
    def validator(f):
        def wraps(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non index'.format(index)
                )
            return f(*args)

        return wraps
    return validator

@check_non_index(1)
def create_list(value, size):
    return [value] * size

