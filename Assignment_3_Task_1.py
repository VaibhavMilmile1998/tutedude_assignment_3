#Taking input number
from math import factorial

a=int(input("Enter a number: "))

def Factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

fact = factorial(a)
print("Factorial of ",a,"is: ", fact)