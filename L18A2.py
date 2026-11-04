#This progam uses the Sieve of Eratosthenes to print all  prime number from zero to n (n is whatever number the user inputs)

def SieveofEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num + 1,p):
                prime[i] = False
        p+=1
    for p in range(2,num + 1):
        if prime[p]:
            print(p)

num = int(input("Please enter a number: "))
print(f"The following are prime numbers up to and including {num}")
SieveofEratosthenes(num)