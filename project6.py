#Basic Calculator
def  add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
    
    
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")


    if choice.lower() == "a":
        print("Addition")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        add(a, b)
    elif choice.lower() == "b":
        print("Subtraction")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        sub(a, b)
    elif choice.lower() == "c":
        print("Multiplication")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        mul(a, b)
    elif choice.lower() == "d":
        print("Division")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        div(a, b)
    elif choice.lower() == "e":
        print("Program Ended!!")
        quit()








