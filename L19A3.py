#Checking Parity and Counting Bits

input("Parity - If last bit is 0, the number is even.If the last bit is 1 it is odd.Press enter ")

for n in [2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    if n & 1:
        print(n," = odd")
    else:
        print(n," = even")

n = int(input("Enter a number: "))
input("Count the 1s - watch as the its drop.Press enter ")
temp = n
while temp > 0:
    print("Binary : ",bin(temp)[2:]," Last Bit: "temp & 1)
print("Total 1s in ",n," = ",bin(n).count("1"))