#Program to find HCF/GCD

#User enters two numbers
numberLarge = int(input("Enter the Larger number: "))
numberSmall = int(input("Enter the Smaller number: "))

if numberLarge < numberSmall:
    print("Please enter the larger number first.")
else:
    #Using Eucliden Algorithm
    while (numberSmall):
       numberstorage = numberSmall
       numberSmall = numberLarge % numberSmall
       numberLarge = numberstorage
       print("The HCF is: ",numberLarge)




