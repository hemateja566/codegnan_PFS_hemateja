#checking palindrome or not
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
    
#checking even or odd number
for i in range(0,101):
    if i % 2 == 0:
        print(f"{i} is even num")
    else:
        print(f"{i} is odd num")
