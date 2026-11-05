#Bits and Binary 

n = int(input("Enter a number: "))
guess = input("Guess what you think the binary is: ")

input("Press enter for the answer   ")
print("Decimal: ",n," Binary: ",bin(n)[2:]," Your Guess: ",guess)

input("AND- Both bits have to be 1.Press enter  ")
print("16 = ",bin(16)[2:])
print("24 = ",bin(24)[2:])
print("16 & 24 = ",16 & 24)

input("OR - at least one of the bits has to be 1 to get 1.Press enter  ")
print("16 | 24 = ",16 | 24)
