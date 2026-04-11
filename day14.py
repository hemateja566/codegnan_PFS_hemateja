'''
recursive fuctions
===================

recursion is a programming technique where a function calls itself either directlyor indirectly to solve a problem by breaking it into smaller ,simpler subproblems.
recursion is especially useful for problems that can be divided into identical smaller tasks, such as mathematical calculations ,tree traversals or divide and conquer algorithms.
'''
'''
def validate_pin(self):
    while self.remaining_attempts>0:
        user_pin=input("enter 4 digit pin:")
        if len(user_pin)==4 and user_pin==self.user_info["atm pin"]:
            print("welcome to the atm")
            return True
        else:
            self.remaining_attempts-=1
            if self.remaining_attempts>0:
                print(f"Invalid pin attempts. attempts left {self.remaining_attempts}")
            else:
                print("card blocked. please contact the customer service")
                return False
  '''
'''
any="python is a language"
vowels_list=[]
consonents_list=[]
def vow_and_con(any,vowels_list,consonents_list):
    for i in any:
        if i in "aeiouAEIOU":
            vowels_list.append(i)
        elif i in " ":
            print("spaces")
        else:
            consonents_list.append(i)
    print(vowels_list)
    print(consonents_list)
            
            
vow_and_con(any,vowels_list,consonents_list)
'''
'''
num=int(input())
count=0
def prime(num,count):
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f"{num} is a prime num")
    else:
        print(f"{num} is not a prime number")
        
prime(num,count)
'''

































