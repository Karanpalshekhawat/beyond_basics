"""
Basic introduction to try except block

finally runs no matter what whether we their is exception or not
    Generally for closing the databases
"""
bad_assignment = 'var'
self_rasising_exception = True
try:
    f = open("file_random_3.txt")
    var = bad_assignment
    if self_rasising_exception:
        raise Exception("Seeing self caught exception impact")
except FileNotFoundError:
    print("File does not exist")
except Exception as e:
    print(e)
else:
    print("Executed if everything successfully runs")
finally:
    print("Finally is exectuted")
