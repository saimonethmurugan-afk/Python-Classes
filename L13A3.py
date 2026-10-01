#List Prediction 
#Space Complexity

n = 9
#List stores the score in memory
#Memory grows as n grows

guess = input("Predict: How many items are in the list if n = 9? :  ")
points = list(range(1,n + 1))
print("Your Guess: ", guess, "  List:  ",points,"  Items: ",len(points))

input("What will happen to the list size when n grows? Press enter to find out  ")
for size in [9,1000,10000,100000,1000000,1000000,100000000,1000000000,10000000000]:
    print(f"n = {size:<10}, List uses: {size:>} items in the memory.")