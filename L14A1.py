#Big-O.What is the Big-O and Theta?
#Methods:Formula,Loop then Double Loop

#Defining n

n = 20

#Using the Formula Method - Quickest

guess = input("Double Loop at n = 20 checks n x n pairs.How many are there? Place your guess and press enter:\n")
input("Formula:one calcuation is done.Press enter to check your guess,the amount of steps taken and the constant time.")
steps = 1
print("Steps =",steps,"-> 0(1) constant time -> steps never change.")

#Using the Loop Method - Mid

input("Loop: one step per item.Press enter to run the calculation.  ")
steps = 0
for i in range(n):
    steps+=1
print("Steps =",steps,"->0(n) linear time -> steps gow with n.")

#Using the Double Loop Method - Slowest

input("Double Loop: checks every pair.Press enter to run the calculation.  ")
steps = 0
for i in range(n):
    for j in range(n):
      steps+=1
print("Steps =",steps,"Your Guess:",guess," -> Quadratic Time = 0(n^2).")

