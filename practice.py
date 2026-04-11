str1="there are multiple ways to sort a problem and have multiple solutions"
str2=str1.split(' ')
print(str2)
count=0
for i in str2:
    if i=="multiple":
       count+=1
print(count)
