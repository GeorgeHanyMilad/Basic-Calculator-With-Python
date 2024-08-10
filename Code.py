# Import Libraries

def Addition (a, b) :
    print(f"{a} + {b} = {a + b}")
    print("Done!\n")
    
def Subtraction (a, b) :
    print(f"{a} - {b} = {a - b}")
    print("Done!\n")
    
def Multiplication (a, b) :
    print(f"{a} * {b} = {a * b}")
    print("Done!\n")
    
def Division (a, b) :
    print(f"{a} / {b} = {(a / b):.2f}")
    print("Done!\n")
    
while True :
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    
    Choice = input("Please enter your choice: ")
    if Choice == "A" or Choice == "a" :
        print("Ok, You Chose 'Addition'")
        First_Number = int(input("Please input first number: "))
        Second_Number = int(input("Please input second number: "))
        Addition(First_Number, Second_Number)
        
    elif Choice == "B" or Choice == "b" :
        print("Ok, You Chose 'Subtraction'")
        First_Number = int(input("Please input first number: "))
        Second_Number = int(input("Please input second number: "))
        Subtraction(First_Number, Second_Number)
        
    elif Choice == "C" or Choice == "c" :
        print("Ok, You Chose 'Multiplication'")
        First_Number = int(input("Please input first number: "))
        Second_Number = int(input("Please input second number: "))
        Multiplication(First_Number, Second_Number)
        
    elif Choice == "D" or Choice == "d" :
        print("Ok, You Chose 'Division'")
        First_Number = int(input("Please input first number: "))
        Second_Number = int(input("Please input second number: "))
        Division(First_Number, Second_Number)
        
    elif Choice == "E" or Choice == "e" :
        print("Finished!\n")
        break
    
    else :
        print("Please enter a valid choice.\n")