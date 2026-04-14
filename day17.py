'''
modules
-------
-->A module in a python is simply file that contain python code (functions,variable,classes)
--> to use modules, we have to use a keyword  called import before the modules
                                              Types of modules
                                             ------------------
                            1.built-in                              2.user-defined




user-defined modules-->in this modules file that contain functions is created seperately by user and called in the another program using the file name

syntax:- import(keyword) file_name
        file_name.function_name(arguments)





import modules
print(modules.div(4,5)
print(modules.mul(5,4))
print(modules.add(6,9))
print(modules.sub(8,9))
print(modules.squa(5))
'''

'''
Built-in or inbuilt
-------------------
-->already these are comes with the installation and they  are ready to use in the program
-->this is developed by the developer

syntax:- import(keyword) file_name
        file_name.function_name(arguments)

import math
print(math.sqrt(100))
'''

import random
num=random.randint(1,100)
user_num=int(input("enter your desired number:"))
print(num)
chances=3
while chances>0:
    if user_num==num:
       print("your guess is correct")
    else:
       print("incorrect")
       chances-=1
       



















          
