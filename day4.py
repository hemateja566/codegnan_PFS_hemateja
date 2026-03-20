'''
operators--> an operator is a symbol that performs operations on one or more values (operands) and produces a result

operators are primarily used:
-->calculate values
-->compare values/inputs
-->make decisions
-->control the program flow

ther are major seven categories of operators in python

-->assignment operators
-->arthimetic operators
-->comparison operators
-->membership operators(in,not in)
-->identity operators(is,is not)
-->bitwise operators
-->logical operators(and,or,not)
'''
'''
#Arthimetic operators-->they perform mathematical operations

#+ -->addition,- -->subtraction, * -->multiplication, / --> division
#** --> exponent, %-->modulus, //-->integer division

a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns the value in float
print(a**b)#returns the exponent value

print(a%b)#modulus division-->returns the remainder
print(a//b)#flooring/integer division-->returns quotient discards float value
'''
'''
num1= int(input("enter the first value:"))
num2= int(input("enter the second value:"))
result=(num1+num2)*4
print("the result is",result)
          
#f-string notation
print(f'the result is {result}')
print(f'the result of {num1} and {num2} is {result},{num1*num2}')


#assignment operators
#-->=assign,+= --> addition assignment,-= --> subtract assignment,*=,/=,%=,//=,**=

#they are majorly used for code repetitions in application usage

a=4
b=3
a+=2 #-->a=a+2
print(a)
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
b/=a
print(b)
b%=a
print(b)
b//=a
print(b)
b**=a
print(b)
'''
'''
#relational or comparison operators --> they always return the boolean values(true/false)
#< less than,> greater than ,>=,<=

a=int(input("ener a value:"))
b=int(input("enter the second value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
'''

'''
#membership operators-->they check for the existance of an object in a collection --> in,not in

a="codegnan"
print(type(a))
print('a' in a)
print('z' in 'saketh')
print('z' not in 'codegnan')

b=[12,6,3,4]
c=int(input("enter the value"))
print(c)
print(c in b)
print(c not in b)
'''
'''
#logical operators-->they are used to combine multiple conditions and,or,not

age=int(input("enter the age:"))
vote_right=True

print(age>=18 and vote_right) #both conditions to be true then only true
print(age>=18 or vote_right) #one conditions is true then result is true
print(not vote_right)
'''
'''
#identity operators --> they chheck the memory location and validate we use
#(id) function it is diffferent from== operator -> is, is not

a=[1,2,3]
b=[1,2,4]
print(a==b)
print(id(a)) #returns the identity of an object
print(id(b))
print(a is b)
print(a is not b)

c=b
print(c)
print(id(c))
print(c is b)
'''
#bitwise operators --> and(&) ,or(|)
a=True
b=False
print(a|b)
print(a&b)

print(5&3)
print(bin(5))#returns binary number

#task --> now you have all operators create a cheker task





















