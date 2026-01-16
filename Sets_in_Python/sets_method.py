collection = set()   #sets element are immutalble but sets are mutalble

collection.add(1)
print(collection)

collection.add(5)
print(collection)

collection.add("siddharth")
print(collection)


collection.add((1,2,4,25))  #tuples can be add but list cannt bxoz list are mutable.
print(collection)


collection.add(2)
print(collection)


collection.remove(2)
print(len(collection))

collection.pop()    #its pop the randome value from set
print(collection)

collection.clear()
print(len(collection))









