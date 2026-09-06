#Armstrong Number Checker
#An Armstrong number is when its digits when cubed seperately and added equal the starting number.

num = int(input("Enter a Number:\n"))

original_num = num
sum = 0

#Count the number of digits
digits = len(str(num))

#Calculate Armstrong sum

while num > 0:
    digit = num % 10
    sum = sum + (digits ** digits)
    num = num // 10

#Check the result

if sum == original_num:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")