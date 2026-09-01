#Factorial numbers
#For example number = 5.Computer should display 5*4*3*2*1 = 120

def recur_factorial(number):
    if number == 1:
        return number
    else:
        return number*recur_factorial(number - 1)

user_number = int(input("Enter the number that you want to see the factorial for: "))

if user_number == 0:
    print("The factorial of 0 = 1.")
elif user_number < 0:
    print("Please use numbers >= 0.Factorials of negative numbers do not exist.")
else:
    print(f"The factorial for {user_number} is ",recur_factorial(user_number))
    