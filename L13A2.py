#Time Complexity

input("Double Loop at n = 4 took 10 steps.Watch it grow.Press enter  ")
for n in [100,1000,10000]:
    input("n = " + str(n) + "  Press enter  ")
    print("steps = ",n * (n+1) //2)