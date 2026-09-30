# Writing Different Algorithms to solve the same problem.

# Every student gets a No.points . Student 1 gets 1 point. Student 2 gets 2 points. Student 3 gets 3 points and so on. This means that every student has exactly one more point than the one before them.



n = 4

guess = input("Total points : 1 + 2 + 3 + 4 = ")

#Algorithm 1 for calculating the equation

input("Formula: 1 calculation.Please enter to continue  ")
total = n * ( n + 1) //2
print("Total =",total,"Steps = ",n)

#Algorithm 2 for calculating the equation

input("Loop: Adds one point every time. Please enter to continue   ")
total = 0
for student in range(1,n + 1):
    total += student
print("Total : ",total,"Steps : ",n)

#Algorithm 3 for calculating the equation

input("Double Loop: Counts all of the points. Press enter to continue  ")
total = 0
steps = 0
for student in range(1,n + 1):
    for point in  range(1,student + 1):
        total += 1
        steps += 1
print("Total : ",total,"Steps : ",steps," Your Guess: ",guess)