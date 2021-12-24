
from pprint import pprint as pp
sunday = [11,12,13,14]
monday = [100,110,120,130]
tuesday = [0,1,2,3]

list_of_list = [sunday, monday, tuesday]

pp(list_of_list)

for item in zip(sunday,monday, tuesday):
    pp(item)

# another way
for item in zip(list_of_list[0],list_of_list[1], list_of_list[2]):
    pp(item)

# best way
for item in zip(*list_of_list):
    pp(item)

transposed_list = list(zip(*list_of_list))
