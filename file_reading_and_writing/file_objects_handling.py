f = open('file_random.txt', 'r')
print(f.mode)

f.close()

# using a context manager, will close the file automatically

with open('file_random.txt', 'r+') as f2:
    print(f2.mode)

"""
We have access to the f2 object even after we have come out the with block
but the file is closed
"""

print(f2.mode)
# print(f2.read()) will throw error


with open('file_random.txt', 'r') as f3:
    # strt = f3.read()
    # print(strt)
    # lines = f3.readlines()
    # print(lines)
    for line in f3:
        print(line, end='')

with open('file_random.txt', 'r') as f4:
    size_to_read = 10
    f_cont = f4.read(size_to_read)
    i = 0
    while len(f_cont) > 0:
        print(f_cont)
        f_cont = f4.read(size_to_read)
        i += 1
        print(f'iterating time {i}')
        print(f4.tell())


with open('file_random.txt', 'r') as rf:
    with open('write_to_it.txt', 'w') as wf:
        cont_read = rf.read()
        wf.write(cont_read)
