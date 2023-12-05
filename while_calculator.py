
on = True
def add():
    print("-----Addition-----")
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a+b)

def subtraction():
    print("----- subtraction -----")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number : "))
    print(a - b)

def multiplication():
    print("-----multiplication-----")
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a * b)

def division():
    print("-----Division-----")
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    print(a / b)

while on:
    operation = input("Please selct the type + , - , * , / ,or q")
    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiplication()
    elif operation == "/":
        division()
    elif operation == 'q':
        on == False
    else:
        print("The operation is not available")


