'''
Encapsulation
--------------
-->the principle of binding data (attributes) and methods that operate on the data into a single unit,which is class
class bank:
    def __init__(self,balance):
        self.__balance=balance

    def deposite(self, amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
Acc=bank(15000)
Acc.deposite(7000)
print(Acc.get_balance())
'''
'''
Inheritance
-----------
-->this allows child class which is also called as sub class to acquire the attributes and methods of a parent class (base class) this is called inheritance

1.single Inheritance
--------------------
-->using single method from the base class in the child class.
class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")
any=child()
any.display()



2.Multiple Inheritance
----------------------
-->A child class inherit from the more than one parent class.. 
-->no need to use the super method or keyword


Super()
-------
--> this is used to call the methods of the parent class from the child class
'''

class father:
    def skill_1(self):
        print("Father:hard working")
class mother:
    def skill_2(self):
        print("Mother:Cooking")
class child(father,mother):
    def skill_3(self):
        print("child:coding")


any=child()
any.skill_1()
any.skill_2()
any.skill_3()

















        
