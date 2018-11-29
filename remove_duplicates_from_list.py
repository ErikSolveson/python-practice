import random

def make_random_list (a):
    b = []
    for i in range(a):
        b.append(random.randint(0,10))
        i += 1
    return b

list1 = make_random_list(10)
print (list1)

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list2 = remove_duplicates(list1)
print(list2)