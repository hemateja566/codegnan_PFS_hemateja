'''
str1="there are multiple ways to sort a problem and have multiple solutions"
str2=str1.split(' ')
print(str2)
count=0
for i in str2:
    if i=="multiple":
       count+=1
print(count)
'''
#python methods:
text = "hello"
print(text.upper())   
print("HELLO".lower())   
print("hello world".title())   
print("python".capitalize())   
print("PyThOn".swapcase())   
text = "  hello  "
print(text.strip())   

print("python".find("t"))   
print("python".index("t"))   
print("banana".count("a"))   
print("I like Java".replace("Java", "Python"))
print("python".startswith("py"))   
print("python".endswith("on"))     
print("abc".isalpha())  
print("123".isdigit())   
print("abc123".isalnum())   
print("   ".isspace())   
text = "a,b,c"
print(text.split(","))
print(text.strip(","))

lst = ["a", "b", "c"]
print(" ".join(lst))   


#python list:
lst = [1, 2, 3]
lst.append("python")
print(lst)

lst = [1, 2]
lst.extend([3, 4])
print(lst)

lst = [1, 2, 3]
lst.insert(1, 10)
print(lst)

lst = [1, 2, 3]
lst.remove(2)
print(lst)

lst = [1, 2, 3]
lst.pop()
print(lst)  

lst.pop(0)
print(lst)

lst = [1, 2, 3]
lst.clear()
print(lst)   

lst = [10, 20, 30]
print(lst.index(20))   

lst = [1, 2, 2, 3]
print(lst.count(2))   

lst = [3, 1, 2]
lst.sort()
print(lst)  
lst.sort(reverse=True)


lst = [1, 2, 3]
lst.reverse()
print(lst)   

lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)   
print(lst)   # [1, 2, 3, 4]

#1.odd or even
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(10))

#2.factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))

#3.prime number
def prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(7))

#4.reverse of a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))

#5.addition in list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_list([1, 2, 3, 4]))

#6.counting vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Python is a programming language"))

#7.palindrome
def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(is_palindrome("madam"))

#8.swap
def swap(a,b):
    a,b=b,a
    return a,b
print(swap(6,7))    

#9.count words in a string
def count_words(s):
    words = s.split()
    return len(words)
print(count_words("Python is very easy to learn"))


#armstrong
def armstrong(n):
    order = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    return "Armstrong" if total == n else "Not Armstrong"
print(armstrong(153))










