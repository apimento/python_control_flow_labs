
def vowelCheck():
    vowels = ["a" , "e" , "i" , "o" , "u"]

    x = input("Choose a letter from the alphabet: ")
    if x in vowels:
        print("The letter", x, "is a vowel!")
    else:
        print("The letter", x, "is a consonant!") 

vowelCheck()