"""
Can run function and methods directly withing the f string
"""

name = 'Karan'
last = 'Shekhawat'

# had to pass variable just once if you are using multiple times
sent = 'My name is {0} {1}, you got it, name is {0}'.format(name, last)

print(sent)

# same thing in format

print(f'My name is {name.upper()} {last.upper()}')

person = {
    'name': 'Karan',
    'age': 28
}
# normal method
sentence = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence)

# using f string

sentence_f = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence_f)

calc = f'4 times 11 is {4 * 11}'
print(calc)

for i in range(1, 5):
    print(f'The value is {i}')

pi = 3.14159265
print(f'Pi is equal to {pi:.3f}')

from datetime import datetime
birthday = datetime(1993, 12, 11)
sent_2 = f'Karan has a birthday on {birthday.strftime("%B, %d %Y")}'
print(sent_2)
