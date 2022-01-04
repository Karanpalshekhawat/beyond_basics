"""
Example of how the with is used in the background

with statement will automatically runs the code within our magic __enter__ method

f is set to return value from our __enter__ method
__exit__ method is run when we exit the with block
"""
import os
from contextlib import contextmanager


class OpenFile():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('file_random.txt', 'w') as f:
    f.write('testing')

print(f.closed)


@contextmanager
def new_way_open_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()


with new_way_open_file('sample_using_context.txt', 'w') as f:
    f.write("Some latin philosophy")

print(f.closed)

"""Can be used to change directory and then again change it to original directory"""


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

"""
No need to change back to original directory, 
perform everything in the
"""
with change_dir('Sample directory'):
    print(os.listdir())
