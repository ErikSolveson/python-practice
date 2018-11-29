a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [1 + i for i in a]

print (b)

print ('s' == 's')


import random

c = random.sample(range(1, 30), 12)
d = random.sample(range(1, 30), 16)
result = [i for i in c if i in d]

print (result)

