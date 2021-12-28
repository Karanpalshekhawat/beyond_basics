"""
Iterators and scenarios where we should use them.
what are the benfits over list

Generators perform much more efficiently,
it is much faster

Memory usage and time taken is very minimal in case of generators
as it does not hold all the values, and just hold the first value.
give numbers one at a time
If you have very large datatypes where you have to use method
try to do it using generators

Lists keep all values in some memory while generator do not, they just
keep the first value in memory
"""

"""normal example"""


def square_numers(ls):
    result = []
    for i in ls:
        result.append(i * i)
    return result


my_nums = square_numers([2, 5, 10, 3, 7])
print(my_nums)

"""
how to do same thin in case fo generator
much more readable
"""


def square_numers_generators(ls):
    for i in ls:
        yield (i * i)


# my_nums_2 is the generator object
my_nums_2 = square_numers_generators([2, 5, 10, 3, 7])
print(my_nums_2)

# best way

for num in my_nums_2:
    print(num)
