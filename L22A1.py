#n & (n -1) trick, power of 2 bitwise check

input("n & (n - 1) clears the rightmost set bit. Press enter...")
print("12 & 11 =",12 & 11," Binary: ",bin(12 & 11)[2:])
print("8 & 7 =",8 & 7)

n = int(input("Enter a number: "))
guess = input("Is " + str(n) + " a power of 2 (Bitwise) ? :")
input("Power of 2: n & (n - 1) == 0 means only one bit is ON.Press enter...")
if n > 0 and (n & (n -1)) == 0:
    print(n," Binary :",bin(n)[2:]," Power of 2: Yes  Your Guess:",guess)
else:
    print(n," Binary :",bin(n)[2:]," Power of 2: No  Your Guess:",guess)
    