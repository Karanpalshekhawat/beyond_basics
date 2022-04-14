"""
Demo for iterables, iterators (there is a difference)

list is iterable but not an iterator
"""

"""
Iterable: something which can be looped over
"""

"""
Iterators: object with a state so that it remembers where it is, __next__ method
"""

"""
For most of dunder methods, we have some function which calls them in the background

like ls.__iter__() can be iter(ls)
and ls2.__next__() can be next(ls2)
"""

ls = [1, 2, 3, 4]
fd = '__iter__' in dir(ls)
dg = '__next__' in dir(ls)  # whether iterators or not

print(fd, dg)

check = '__next__' in dir(ls.__iter__())
print(check)

i_ls = iter(ls)
print(dir(ls))

print(next(i_ls))

"""
StopIteration exception when it runs out of values

only go forward, if want to start scratch, make new iterable
"""

while True:
    try:
        j = next(i_ls)
        print(j)
    except StopIteration:
        print("list is ended")
        break
