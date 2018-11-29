a = [5, 10, 15, 20, 25]


def get_first_and_last (a):
    i = len(a)
    print (i)
    b = [0, a[i - 1]]
    return b

b = get_first_and_last(a)
print(b)