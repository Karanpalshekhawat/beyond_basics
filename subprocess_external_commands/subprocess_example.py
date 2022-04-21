import subprocess


"""
Because in mac, windows we have to use dir, we may have to give
one more command in such as shell=True because dir command is built into shell

In windows = subprocess.run("dir", shell=True)

Shell = True just means that you can give arguments as it as in a single string
        write exactly same as you will write in a shell format
"""

subprocess.run('ls')

subprocess.run(['ls', '-la'])  # second one is argument

# capture variable in an output instead

p1 = subprocess.run(['ls', '-la'], capture_output=True)
print(p1.stdout.decode())

p2 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(p2.stdout)  # no need to use decode

p3 = subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(p3.stdout)

# Logging
with open('test.txt', 'w') as f:
    p4 = subprocess.run(['ls', '-la'], stdout=f, text=True)

"""
Python does not throw exception if something does not works in subprocess or 
if external commands fail or
error like file does not exist, command not found, it just returns non zero code
You can pass check=true to capture it within code it self
"""

p5 = subprocess.run(['ls', '-la', 'bjhbf'], capture_output=True, text=True)
print(p5.stderr)


"""
Grep is used to search the files for some contents
"""