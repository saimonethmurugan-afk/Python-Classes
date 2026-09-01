#Programme to check if a number inputted is prime
#Taking input from user
num = int(input("Enter your number: "))
if num > 1:
    #Loop only upto the square root of num for efficiency.
    for i in range(2, int(num**0.5) + 1):
        #If num is divisible by any number it is not prime.
        if num % i == 0:
            print(f"{num} is not a prime number. ")
            break
    else:
        #If no divisors were found,number is prime
        print(f"{num} is a prime number. ")
else:
    #Numbers less than 2 are not prime
    print(f"{num} is not a prime number")
