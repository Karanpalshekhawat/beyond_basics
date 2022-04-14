"""
Example why we need to know about iterables or need to make one

we can add __next__ and __iter__ in our own class and make our class iterbale
"""

from time import sleep


class myRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


nums = myRange(5, 9)

# type(nums)
print(list(nums))

# define again
nums = myRange(5, 9)

for num in nums:
    print(num)

sleep(1)


# print(next(nums))    This will give error because next is all finished and we have reached StopIteration

def my_rang(start, end):
    current = start

    while current < end:
        yield current
        current += 1
