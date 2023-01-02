import math 
def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n -4)

n=int(input("Enter number of inputs: "))

for i in range(0,n):
    x=int(input("Enter the number: "))
    if (x<0):
        print("Please enter positive number")
    else:
        if (isFibonacci(x)==True):
            print(x,"is valid number in Fibonacci series")
        else:
            print(x,"is not valid number in Fibonacci series")