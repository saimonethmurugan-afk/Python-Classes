#Not , XOR , Left shift and right shift

n = int(input("Please enter a number: "))

guess = input("Left shift doubles it. What is your guess? : ")

input("NOT - Flips every bit.Press enter ")
print("8 = ",bin(12)[2:])
print("NOT 8 =",~8 & 0xFF)

input("XOR - Different bits result in 1.Press enter ")
print("8 ^ 10  =",8^10)

input("Left shift - Multiplies the number by 2.Press enter ")
print(n," << 1 =",n << 1)

input("Right shift - divides by 2.Press enter ")
print(n, ">> 1 =",n >> 1)