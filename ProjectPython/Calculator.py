# calculator
import os


# Operator function
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

operator= {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

def calculator():
    #getting input from User
    num1= float(input("Enter first number: "))

    continue_flag=True

    while continue_flag:

        for symbol in operator:
            print(symbol)

        select_operator=input("Select an operator : ")

        num2= float(input("Enter second number: "))

        # programming start
        calculator_function=operator[select_operator]

        output= calculator_function(num1,num2)

        # Final output
        print(f"{num1} {select_operator} {num2} is {output}")

        should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation  or or 'x' to exit").lower()
        if should_continue=='y':
            num1=output

        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()

        elif should_continue=='x':
            continue_flag=False
            print("bye")

calculator()
