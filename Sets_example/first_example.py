"""
Examples of set, intersection, union best
"""

s1 = set([1, 2, 3, 4, 5])
s2 = {1, 2, 3, 42, 5}  # also a set
print(s1)
print(s2)

s1.add(7)
s1.update([4, 8, 9, 8, 9], s2)
print(s1)

s1.remove(5)
print(s1)

s3 = {1, 2, 3}
s4 = {2, 3, 4}
s5 = {3, 4, 5}

s6 = s3.intersection(s4)
s7 = s4.intersection(s5)

print(s6, s7)

s9 = s3.difference(s4)
s10 = s4.difference(s3)

print(s9, s10)

s11 = s4.difference(s3, s5)
s12 = s5.difference(s3, s4)

print(s11, s12)

s13 = s3.symmetric_difference(s4)  # all differences
print(s13)

"""remove duplicates"""

l1 = [1, 2, 1, 3, 3, 1, 2, 4, 5, 4]
l2 = list(set(l1))

print(l2)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

# both in gym members and developers
print(list(set(gym_members).intersection(set(developers))))

print((set(employees).difference(gym_members)).difference(set(developers)))

# same thing

print(set(employees).difference(gym_members, developers))
