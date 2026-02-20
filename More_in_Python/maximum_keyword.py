from functools import reduce
l = [10, 25, 8, 99, 3]

max_num = reduce(lambda a,b: a if a > b else b,l)

print(max_num)