#Power of 4,Power of 8,Bit position


input("Power of 4:n % 3 == 1     Power of 8: n % 7 == 1. Press enter...")
print("16 Binary: ",bin(16)[2:]," 16 % 3 =",16 % 3,"Power of 4: Yes.")
print("8 Binary: ",bin(8)[2:]," 8 % 7 =",8 % 7,"Power of 8: Yes.")

n = int(input("Enter a number: "))
guess = input("Is " + str(n) + " a power of 4 (Bitwise) ? :")
input("Power of 4: n & 3 == 1. Press enter...")
is_pow4 = n > 0 and (n & (n - 1) == 0 and n % 3 == 1)
if is_pow4:
    print(n," Binary :",bin(n)[2:]," Power of 4: Yes  Your Guess:",guess)
else:
    print(n," Binary :",bin(n)[2:]," Power of 4: No  Your Guess:",guess)