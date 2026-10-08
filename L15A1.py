#Using Binary Search
#Binary Search is when the computer halves the problem so that it can find the number more efficiently.

scores = [1,4,6,9,23,43,67,78,34,11]

input("List:"+str(scores)+"   n = 10.  PRESS ENTER......")
guess = input("What is your guess?How many checks do YOU think it will take me to find any number in this list? : ")
target = int(input("Pick a number for me to find from the list:  "))

input("Binary Search- checks which number is in the middle,drops half of it every single try.Press enter to start the program.....")
low,high = 0,len(scores)-1
steps = 0
while low<=high:
    medium = (low+high)//2
    steps+=1
    print("Round Number:",steps,"-> checked",scores[medium])
    if scores[medium] == target:
        break
    elif scores[medium]<target:
        low = medium + 1
    else:
        high = medium -1
print("Found: ",target,"At Position:",medium+1,"In ",steps," steps  Your Guess:",guess," -> 0(log n)")

input("Steps grow visibly with n.Press enter...........")
for n,s in [(9,3),(43,5),(11,9)]:
    print("n = ",n,"  Maximum steps =",s," -> 0(log n)")