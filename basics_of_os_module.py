"""
Details about how to best use os module
"""

import os

print(os.getcwd())

os.chdir('/Users/karanpalsinghshekhawat/Desktop/')

print(os.getcwd())
print(os.listdir())
# mkdir and makedirs to make directory, second one will help if we want to create subdirs like dir1/dir2/dir3
# same rmdir and removedirs

#os.makedirs('demo1')
# os.stat(filename) will give details about the file

print(os.walk(os.getcwd())) # generator object
"""Directory name and filenames within the directory"""
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('current path is {0}'.format(dirpath))
    print('Directory name is {0}'.format(dirname))
    print('Filenames are {0}'.format(filename))
    print()


# All paths in environment
print(os.environ.get('PATH'))
# path joins, helps in handy when we don't know where to add slashes
os.path.join("path1", "path2")


"""
os.path.splitext("filename") for removing the extension of the file
"""