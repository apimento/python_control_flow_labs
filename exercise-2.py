def charCounter():
    while True:
        string=input("Tell me something:")
        if string == "quit":
            break
        else:
            print("Your phrase is", len(string), "characters long") 

charCounter()