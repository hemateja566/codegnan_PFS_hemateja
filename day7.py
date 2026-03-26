'''
Time_aday=input("enter 24 hours time:")
parts_=Time_aday.split(":")
hours_=int(parts_[0])
min_=int(parts_[1])
if hours_>=13 and min_<60:
    print(f"{Time_aday} convert into {hours_-12}:{min_}pm")
else:
    print(f"you have entered nrml or the min is incorrect")
'''
'''
#List--->Different types inside the '[]', which are seperated by ',' and it is mutable
#example-->[1,"name",[1,2,"Teja"]]

List_1=[1,2,3,"Python",[1,2,["Python","Java"],"Language"]]
print(List_1[4][2][0][3])
List_2=["frog","cat",3,5,["teja",["school",1,8],"fox"]]
print(List_2[4][1][0][4])
List_5=[4,5,"ram",["shekar",[4,5,"shiva"],79],89,"puja"]
print(List_2[4][1][0][2])
List_3=["thanuja","harshitha","cat",3,5,["teja",["school",1,8],"fox"]]
print(List_2[2][1])
List_4=["aeroplane","cat",3,5,["dog",["school",1,8],"fox"],67]8,9]
print(List_2[4][3][0])
'''
#methods of List
'''---------------
append()--> used to add new items into list,it will only go to the last index of the list
Syntax-->variable_name.append(item)

extend()-->used to add items in the last index,where each item are substring in each index in the list
Syntax-->variable_name.extend(item)

remove()--> this method will delete the item or value directly
Syntax-->variable_name.remove(item)

pop()--> pop the items using the indices
Syntax-->variable_name.pop(index_number)
'''
'''
List=[1,2,3,4,5]
print(List)
List.append(67)
print(List)
List.append(678)
print(List)
List.append([23,96])
print(List)
List.extend("teja")
print(List)
List.extend([23.0,27.0])
print(List)
List.remove(5)
print(List)
List.pop(4)#using indexes
print(List)
'''
