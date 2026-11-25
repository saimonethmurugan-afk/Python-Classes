#XOR Identity and Equality


# XOR Equality

input("XOR with 0 keeps the number same.Press enter.....")
print("5 ^ 0 = ",5 ^ 0)
print("9 ^ 0 = ", 9 ^ 0 )

#XOR Identity

input("XOR with the same number is 0.Press enter....")
print("5 ^ 5 = ",5 ^ 5)
print("9 ^ 9 = ",9 ^ 9)

n = int(input("Enter a number: "))
guess = int(input("What would 3 ^" + str(n) + "^ 3 equal ?"))
input("XOR cancels out the 3s because 3 appears twice.Press enter....")
print("3 ^",n," ^ 3 =",3 ^ n ^ 3," Your Guess: ",guess)
