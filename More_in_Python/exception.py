try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


try:
    with open(r"E:\Scratch.python\More_in_Python\2.txt", "r") as f: #here file is created so i have pasted the file link with 'r' bcoz of \2. <- excape sequence.
        print(f.read())
except Exception as e:
        print(e)


try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
        print(e)

print("Thank you!")
