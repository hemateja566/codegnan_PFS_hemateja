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
