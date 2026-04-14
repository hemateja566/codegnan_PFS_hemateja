#factorial of a number
x=int(input())
def factorial(x):   
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
factorial(x)
print("The factorial of", x, "is", factorial(x))
