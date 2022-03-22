def calcDogYears(): 
    x = int(input("Enter dog's age in human years:"))
    if x > 2:
        firstTwo = 20
        remYears = x - 2
        calcRemYears = remYears * 7
        print("The dog's age in dog years is:", (calcRemYears + firstTwo))
    elif x <= 2:
         print("The dog's age in dog years is:", x * 2)

calcDogYears()


