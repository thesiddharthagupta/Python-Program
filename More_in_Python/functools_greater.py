from functools import reduce
l = [111, 125, 236, 34, 56, 69]

def greater(a,b):
    if (a>b):
        return a
    return b

print(reduce(greater,l))