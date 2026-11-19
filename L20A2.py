#The first set bit

input("First set bit: The rightmost 1 in a binary number.Press enter ")
print("5 = Binary: ",bin(5)[2:]," First 1 position 0.")
print("8 = Binary: ",bin(8)[2:]," First 1's position is 3")

n =  int(input("Enter a number: "))
input("Watch the bits drop until the first 1 bit appears.Press enter  ")
temp = n
pos = 0

while temp > 0:
    print("Binary: ",bin(temp)[2:]," Last Bit: ",temp & 1)
    if temp & 1:
        break
    pos += 1
    temp >>= 1
print("First set this bit in ",n," is at position ",pos)