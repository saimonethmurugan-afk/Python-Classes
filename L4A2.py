
#Printing a star pattern
i = int(input("Enter how many rows you want: "))
for b in range(1,i + 1):
    #It will print a star and end with space instead of a new line
    for c in range(b):
        print('*', end = ' ')
    #After each row it will print a new line
    print()
    