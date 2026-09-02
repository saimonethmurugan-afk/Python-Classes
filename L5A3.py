#Addition
def add(x,y):
    return x + y
#Subtraction
def subtract(x,y):
    return x - y
#Multiplication
def multiply(x,y):
    return x * y
#Division
def divide(x,y):
    return x / y

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter your second number: "))

print("Sum: ",add (number1,number2))
print("Difference: ",subtract(number1,number2))
print("Product: ",multiply(number1,number2))
print("Quotient: ",divide(number1,number2))