'''
Multi-level inheritance
-----------------------
This occurs when a class inherit from the child class,creating a grand parent
grand parent-->parent--> child in this structure

class Grandparent:
    def show_Grandparent(self):
        print("I'm Grand parent")

class Parent(Grandparent):
    def show_Parent(self):
        print("I'm a parent")

class child(Parent):
    def show_child(self):
        print("I'm a child")

any=child()
any.show_Grandparent()
any.show_Parent()
any.show_child()
   '''       
class mobile:
    def mobile_upgrade(self):
        print("mobile upgraded")

class system(mobile):
    def system_upgrade(self):
        print("system is good")

class application(system):
    def app_upgrade(self):
        print("apps are updated")



'''
Hierarchial
-----------
-->this occcurs when multiple child classes inherit from a single parent class, this process is called hierarchial

class parent:
    def _parent(self):
        print("I'm Grand parent")

class child_1(parent):
    def _child(self):
        print("I'm a child 1")

class child_2(parent):
    def child_(self):
        print("I'm a child 2")

class child_3(child_1,child_2):
    def child(self):
        print("I'm child")

obj=child_3()
obj._parent()
obj._child()
obj.child_()
obj.child()

hybrid inheritance

------------------
-->This is a combination of two or more types of inheritance,such as single,multiple,
multi-level ,or hirerarchiel all this in a single class...
'''
class parent:
    def _parent(self):
        print("I'm Grand parent")

class child_1(parent):
    def _child(self):
        print("I'm a child 1")

class child_2(parent):
    def child_(self):
        print("I'm a child 2")

class child_3(child_1,child_2,application):
    def child(self):
        print("I'm child")

obj=child_3()
obj._parent()
obj._child()
obj.child_()
obj.child()
obj.app_upgrade()
obj.system_upgrade()
obj.mobile_upgrade()


































