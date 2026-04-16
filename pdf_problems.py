
#area of rectangle 14-4-2026
def area(l,b):
    return l*b
l=int(input())
b=int(input())
print(area(l,b))

#greetings 14-4-2026
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}! You are {age} years old.")

#odd or even 15-4-2026
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num=int(input("enter a num:")
print(even_odd(num))

#minimum and maximum   15-4-2026
numbers = list(map(int,input().split()))
numbers.sort()
minimum = numbers[0]
maximum = numbers[-1]
print(f"minimum={minimum} maximum={maximum}")
