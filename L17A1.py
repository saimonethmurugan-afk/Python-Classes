#Taking input from the user
number = int(input("Please enter the number: "))

#Store number in another variable for later comparison
original_number = number
reversed_number = 0

#Reversing the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

#Checking if the orignal number and the reversed number are the same

if original_number == reversed_number:
    print(f"{original_number} is a palindrome number.")
else:
    print(f"{original_number} is not a palindrome number.")

