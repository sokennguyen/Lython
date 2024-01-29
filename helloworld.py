import random
import copy

print('hello, world')
myName = 'hihi'
print(myName)
print('length = ' + str(len(myName)))

spam = True
print(spam)

for i in range(5):
    print(i)

for i in range(5):
    print(random.randint(1, 69))

spam = ['first', 'second', 'last']
print(spam[-1])

print(random.choice(spam))
random = random.shuffle(spam)
for i, item in enumerate(spam):
    print(item, end=', ')

stri = 'hihi'
stri += 'haha'
print(stri)
print(id(stri))

spam.append(['extra', 'list'])
cheese = copy.deepcopy(spam)
print(cheese)
