'''required arguments
   ------------------
 -->it should match the same number variables in calling with def
 
Default arguments
=================
-->it will take  the default values from the arguments

num = 9
num_2 = 10
def add(num,num_2):
   print(num+num_2)
add(num,num_2)

my_name="hema teja"
def add(my_name):
    print(my_name)
add(my_name="kosana") 
   
   

def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
       print(f"{num} it is a prime")
    else:
       print(f"{num} it is not a prime")
    
prime(num =37)
prime(num=40)

def any(num, num_2):
    print(num,num_2)
any(num_2=7,num=0)
'''

def series(*names_):    # '*' is used to read the multiple values in arguments
    print(names_)
    print(names_[1])
series("hema" ,"teja","reddy")
