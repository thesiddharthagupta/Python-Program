def division(n):
    if(n%5 == 0):
        return True
    return False

a = [5,2,25,166,646,4565,5464,7970,46464]

f = list(filter(division,a))
print(f)