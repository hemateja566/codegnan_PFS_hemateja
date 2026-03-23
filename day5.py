'''
condition statements:-->
if statement-->this (if statement) is used to check any condition becomes true then it will enter in side the (if statement

age=int(input("enter your age:"))
if age>=18:
    print("your age is 18 or above")

product_price=int(input("enter the product price:"))
if product_price>=100:
    print("the product is not cheaper")
'''          

#if-else statement--> this also called as fall back statement
#which only execute when the (if stament) becomes false
'''
age=int(input("enter your age:"))
if age>=18:
    print("you can vote")
else:
    print(f"you cannot vote and have to wait {18-age} yrs to vote")
'''
'''
total_amount=int(input("enter the total shopping money:"))
if total_amount>=149:
    print("No deliver cost")
else:
    print(f"add {149-total_amount} to your cart")
    '''
'''
marks=int(input("enter  the marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")
  '''              
'''
#if-elif-else statement-->in the elif part i check one more condition and can be said as combination of if and  else
student_marks= int(input("enter your marks:"))
if student_marks >=90:
    print("you got A+ grade")
elif student_marks >=75 and student_marks<90:
    print("you got A grade")
elif student_marks >=65 and student_marks<75:
    print("you got B+ grade")
else:
    print("you are fail")
'''
'''
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
operation=input("enter the operation:")
if operation==+:
    print(f"{num1+num2}")
elif operation==-:
    print(f"{num1-num2}")
elif operation==*:
    print(f"{num1*num2}")
else:
    print("chose correct option")

 '''   
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
operation=int(input("enter the operation \n1.add \n2.sub \n3.mul \n4.div:"))
if operation==1:
    print(f"{num1+num2}")
elif operation==2:
    print(f"{num1-num2}")
elif operation==3:
    print(f"{num1*num2}")
elif operation==4:
    print(f"{num1/num2}")
else:
    print("chose correct option")

'''
code Q
'''
