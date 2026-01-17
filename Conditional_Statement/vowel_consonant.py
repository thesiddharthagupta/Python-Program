'''
Write a program to check whether a character is a vowel or consonant.

'''

check = input("Enter a letter: ")
if check.lower() in ["a", "e", "i", "o", "u"]:
    print("Entered number is Vowel: ", check)

else : 
    print("the number is consonent: ", check)


