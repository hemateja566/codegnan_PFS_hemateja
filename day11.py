
#get prime numbers from 2 to 100
for i in range(2,101):
    count=0
    for j in range(1,i+1):
        if i % j==0:
           count+=1
    if count==2:
       print(f"{i} is a prime number")
    else:
       print(f"{i} is not a prime number")

list1=[1057,197,9,86,17673]
for i in list1:
    count=0
    for j in range(1,i+1):
        if i % j==0:
           print(j)
           count+=1
    if count==2:
       print(f"{i} is a prime number")
    else:
       print(f"{i} is not a prime number")

#removing duplicates
any=[2,356,8,6,3,2,8]
an=[]
for i in any:
    if i not in an:
        an.append(i)
    else:
        break
    print(an)

#armstrong number
so=int(input("enter a number:"))
length_=len(str(so))
amstr_=0
for j in str(so):
    amstr_+=int(j)**length_
    print(amstr_)
if amstr_==so:
    print(f"{so} is armstrong number")
else:
    print(f"{so} is not armstrong number")









    
