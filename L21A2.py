#Odd occuring number

input("XOR all numbers - pairs of numbers cancel each other out, the odd one stays.Press enter....")
print("List: [2,3,4,2,3]")
print("Odd occuring:",2^3^4^2^3)

n = int(input("Enter a number: "))
nums = [3,n,3,5,5]
guess = input("Which number in " + str(nums) +"appears only once? : ")
result = 0

for x in nums:
    result ^= x
input("XOR cancels pairs.The odd one survives.Press enter....")
print("List: ",nums," Odd occuring: ",result," Your Guess: ",guess)