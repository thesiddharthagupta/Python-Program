num = int(input("Enter a number: "))

if num <= 1:
    print("Neither prime nor composite")
else:
    count = 0

    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        print("Prime number")
    else:
        print("Composite number")
