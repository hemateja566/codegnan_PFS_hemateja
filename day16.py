'''
#generators
--------------
--> This is a special type of function that return a iterator which one at a time
--> 'yield' ==>it will take a pass and again resume,this is not a nrml keywoord cant be used in the nrml functions
--> this is used to produce a value and pause execution.

Next()
---------
--->This is used to get next value from a generrator
--->when the value is finished ,it will stop the iterator

def my_generator():
    yield 1
    yield 2
    yield 3
an = my_generator()

print(next(an))
print(next(an))
print(next(an))
'''
def square_gen(n):
    for i in range(n):
        yield i*i

for val in square_gen(5):
    print(val)

def addition_gen(n):
    for i in range(n):
        yield 10+i

for val in addition_gen(20):
    print(val)

for j in range(20):
    print(j)










    
