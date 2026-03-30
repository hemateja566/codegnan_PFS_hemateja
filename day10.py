'''
for loop:- is used for getting,checking the values in sequence
 'i' is an initial variable that it can be initialised directly in the loop
ex:-
a=9
print(b)
for j in range(1,10):
    print(j)

range()--> this is used to generate numbers
syntax-->range(start,end,step)
'''
#for j in range(10,100,4):
 #   print(j)
'''
any="123"
print(int(any))
print(tuple(any))
print(list(any))
print(str(any))
print(float(any))

an=[1,2,3]
print(tuple(an))

a=[(1,2),(3,4)]
print(dict(a))
'''
'''
str1="hemateja"
str2=str1[::-1]#reversing with '::-1'
print(str2)

str3=""
for i in str1:
    str3=i+str3 #reversing the string without '::-1'
    print(str3)
if str1==str3:
    print(f"{str1} is a palindrome")
else:
    print(f"{str1} is not a palindrome")
'''

for i in range(0,101):
    if i % 2 == 0:
        print(f"{i} is even num")
    else:
        print(f"{i} is odd num")
    
