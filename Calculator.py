import math

print("Select an opertion from(1--6)")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")

operation = input()

if operation == "1": # PERFORM ADDITION
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": # PERFORM SUBTRACTION
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3": # PERFORM PRODUCT
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4": # PERFORM DIVISION
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5": # PERFORM SQUARE ROOT
    num = int(input("Enter the number: "))
    print("The square root is %f " + %(math.sqrt(num)))
elif operation == "6": # SQUARE A NUMBER
    num = int(input("Enter the number: "))
    print("The result is %d " + %(pow(num, 2)))
else:
    print("Invalid entry")