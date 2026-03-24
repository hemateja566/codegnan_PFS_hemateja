'''String ---> Sting is a collection of characters,which represented by "" or ''
and we can access it using indexing and also slicing'''
'''
any ='teja2004@'
print(any[5])
#slicing
print(any[5:8])

#this is also immutable data type,where i could not able to modify on that particular variable
any='python programming'
so=any.replace("python","java")
print(any)
print(so)

#negative indexing
print([-5])

#out of range error
print([100])
'''
'''
a_day="I'm Teja from vizianagaram,currently enrolled in python fullstack  at  codegnan "
print(f"my name is {a_day[5:8]}")
print(f"place is {a_day[14:26]}")
print(f"institute is {a_day[-9:-1]}")
'''
'''
#reverse
day='teja'
print(day[::-1])

#len()-->find the of the string
print(len(day))
'''
'''
#note--> we cannot convert string to integer or float can only be converted if the string contains only numbers

some='123'
num=int(some)
print(type(num))
'''
'''
#methods
#1.split()-->remove space by default and the output is in the list[] it will give the seperated thing in each index
#syntax-->variable_name.split("substring")
some="python is a programming language"
print(some.split(" "))
print(some.split())

#lower()-->converts every thing into lower case
#syntax-->variable_name.lower()
some="Python is a Programming Language"
print(some.lower())

#upper()-->converts the entire string into uppercase
#syntax-->variable_name.upper()
print(some.upper())

#join() --> joints the two strings
#replace()-->replace a substing
some="Python is a Programming Language"
print(some.replace("Python","java"))
'''
'''
some="python is a programming language"
if "is" in some:
    print("it contains")
else:
    print("doesn't contain")
'''
user_input=input()
if user_input in "aeiou":
    print("vowel")
else:
    print("consonent")
