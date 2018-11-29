__author__ =  'Erik Solveson'

num = int(input("Number you would like the divisors for: "))
b = []
x = range (1, num+1)

for i in range(len(x)):
    if num % x[i] == 0:
        b.append(x[i])

print(b)