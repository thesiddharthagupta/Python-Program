# by parameter pasing as "a"
num = int(input("Enter a number: "))

def table(a):
    i = 1
    while i <= 10:   # loop runs until i reaches 10
        print(f"{a} X {i} = {a * i}")
        i += 1       # increment i each time

table(num)


                            
                            # < another method >
# by without parameter

# num = int(input("ENter a number: "))
# def table(num):
#     i = 1
#     while i<=10:      # loop runs until i reaches 10
#         print(f"{num} X  {i} = {num*i}")
#         i += 1        # increment i each time
# table(num)