#This program checks if a number inputted by the user is prime or not.

#Importing the Math library which is built in to Python
from math import sqrt

number = int(input("Please enter the number: "))

#Checking if the number is greater than one
if number > 1:

    #Check if the number is divisible by 2 or anything else which would not make it a prime.
    for i in range(2,int(sqrt(number))+1):

        #Printing if the number is prime or not.
        if (number % i) == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")

else:
    print(f"{number} is not a prime number.")