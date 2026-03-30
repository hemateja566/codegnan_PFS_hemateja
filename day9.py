'''
We can store data as key : value
Keys ---> are unique and we can only give immutable data types in the keys
Values---> we use all datatypes(mutable and immutable)

methods
--------------
keys()---this is used to get all keys from the dict
values()---this method is used to get all values from the dict
clear()---this method is used to delete the dict
'''

sbi_teja={"name":"Teja",45:67,(4,7):"hema"}
print(sbi_teja['name'])      
print(sbi_teja.keys())
print(sbi_teja.values())
print(sbi_teja.clear())
print(sbi_teja)


#set{}---> set is an unordered collection and it won't allow duplicates
#union()---> this is used to add or get 2 different sets without duplicated
#intersection()--->this is used to get the common from the both sets
#difference()--->this is used to get the difference of the 2 sets
any={1,2,3,4,2}
so={4,5,6}
print(any)
print(so)
print(any.union(so))
print(any.intersection(so))
print(any-so)
print(so-any)
print(any.difference(so))
any.remove(4)
print(any)
any.pop()
print(any)

#check if the pin  is correct or not

profile={"name":"teja",
         "pin_no":4089,
         "salary":40000,
         "emp_id":"A43G566"}
pin=int(input("enter the pin:"))
if pin == profile['pin_no']:
    print(profile)
else:
    print("enter correct pin")
