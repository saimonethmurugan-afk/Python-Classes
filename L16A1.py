#What are Armstrong Numbers?
#Armstrong numbers are numbers that if their digits were calculated to the power of the total amount of digits and added up it would still equal the intial number.
#This program checks if a number is Armstrong or not.

print("Hello!Press enter to check if a number is Armstrong or not.")

number = int(input("Please enter the number: "))

#Calculating how many digits are in number
no_digits = len(str(number))

FinalNum = 0

#Using the formula to find out if the number is Armstrong

temp = number
while temp>0:
    digits = temp % 10
    FinalNum += digits**no_digits
    temp //=10

if number==FinalNum:
    print("This number is an Armstrong number.")
else:
    print("It is not an Armstrong Number.")

    
    
