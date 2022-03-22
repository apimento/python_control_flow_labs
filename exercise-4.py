def typeOfTriangle(): 
    a = int(input("Enter the length of the triagle's first side: ")) 
    b = int(input("Enter the length of the triagle's second side: "))  
    c = int(input("Enter the length of the triagle's third side: "))  
    if a == b == c:
        print("Your triangle is equilateral") 
    elif a == b or b == c or a == c:
        print("Your triangle is isosceles")
    else:
        print("Your triangle is scalene") 

typeOfTriangle()