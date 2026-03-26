
print(3+4)
print("python"+" language")
print([1,2]+[3,4])
'''
concatination
=================
this is nothing but, a (+) behavi...
case-1
------------------
integers---this wiill act as addition for the int

case-2
------------------
for other data types  (we have to use same type) this (+) act as concatination
'''
#print("hema"+[1,2])
#note:can only concatenate str (not "list") to str ,cannot able to concatinate two different data types
#print(1+"teja")
#print(2.0+[1,2])
'''
tuple()--->
----------------------
it is a collection of differet datatypes and this is represented by '()',seperated by ','
eg...
Thing=(1,"Teja",[12,4],(6,7))
'''
#Thing=(1,"Teja",[12,4],(6,7))
#print(Thing)
Thing=(12,89,"python",(23,"Teja",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(Thing[3][2][1][9])


#Swapping of numbers without using third variable
Num=9
Num_2=90
print(f"before swapping Num={Num} and Num_2={Num_2}")
Num,Num_2=Num_2,Num
print(f"after swapping Num={Num} and Num_2={Num_2}")

#Checking leaf year or not program
Leap_year=int(input("Enter year:"))
if (Leap_year % 4==0 and Leap_year%100!=0) or Leaf_year % 400==0:
    print(f"yes,{Leap_year} is a leap year")
else:
    print(f"no,{Leap_year} is not a leap year")
          
