
While True:
    
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Clear")
    print("6. Exit")

    option = input("Select an operation and press enter: ")

    if int(option) == 1:
    
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        sum = num1 + num2
        print(sum)

    elif int(option) == 2:
    
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        sub = num1 - num2
        print(sub)

    elif int(option) == 3:
    
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        divide = num1 / num2
        print(divide)

    elif int(option) == 4:
    
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        multiply = num1 * num2
        print(multiply)

    elif int(option) == 5:
    
        print("Calculator cleared")

    elif int(option) == 5:
    
        print("Existing calculator")
        break

    else:
        print("Invalid operation,enter a number between 1 and 6.")
    
