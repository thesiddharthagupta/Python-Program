a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("the triangle is Equaliteral")
    elif a == b or  b == c or c == a:
        print("the triangle is isolateral") 
    else:
        print("the triangle is scaler")
else:
    print("not a valid  traingle")
