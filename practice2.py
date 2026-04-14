'''
str1="Python is a Programming Language"
print(str1.split())
print(str1.upper())
print(str1.replace("Python","Java"))
print(str1.isalpha())
print(str1.isalnum())
print(str1.isdigit())
print(str1.swapcase())
print(str1.capitalize())
print(str1.lower())
print(str1.index("a"))
print(str1.find("a"))

'''


#list methods
list_1=[ 1, "python", ["is","mode" ,4],{"hi",1}]

list_1.append("java")
list_1.append([4,5])
print(list_1)


list_1.extend([4,3])
print(list_1)

list_1.insert(5,2)
print(list_1)

list_1.pop()
print(list_1)

print(list_1.count(1))

print(list_1.index("java"))


list_1.clear()
print(list_1)

list_2=[4,6,5,9]
list_2.reverse()
print(list_2)

list_2.sort()
print(list_2)


list_3=["java","python","program"]
list_3.sort()
print(list_3)


