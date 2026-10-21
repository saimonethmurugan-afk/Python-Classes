#Finding the factors of a user inputted number.

#Defining our function
def factor(number):
    print("The factors of ",number," are: ")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

#Taking input from the user
number = int(input("Please enter the number you would like me to find the factors for: "))


#Calling our function
factor(number)



























