#Setting bits and zero bits,Checking power of 2

input("Setting a bit - OR turns it ON.Press enter ")
print("5 = ",bin(5)[2:])
print("5 | 2 =",5|2,"Binary: ",bin(5|2)[2:])

input("Zeroing a bit - AND turns it OFF.Press enter ")
print("7 = ",bin(7)[2:])
print("7 & 5 =",7&5,"Binary: ",bin(7&5)[2:])

n = int(input("Enter a number: "))
guess = input("Is it a power of 2 (Yes/No)?:  ")
input("Power of 2 - only one bit is ON.Press enter ")
if n > 0 and (n & (n-1)) == 0:
    print(n," Binary :",bin(n)[2:]," Your Guess for Power of 2: ",guess)
else:
    print(n," Binary: ",bin(n)[2:], "Not Power of 2 Your Guess: ",guess)