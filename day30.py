'''
import re
def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    patter = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[a-z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)

def main():
    name = input("Enter Name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    if not validate_name(name):
        print("Invalid Name")
    elif not validate_email(email):
        print("Invalid Email")
    elif not validate_phone(phone):
        print("Invalid phone number")
    elif not validate_phone(password):
        print("Invalid password")
    else:
        print("all inputs are valid! from submitted successful")
if _name_ == "_main_":
    main()

()

why this is need?
----------------
-->this is critical bcoz it converts rew data into actionable insights, enabling information to
decision-making easy and import
operational efficiency....

1.decision-making
2.improved operational efficiency
3.customer understanding
4.market insight
5.risk management
6.data-driven strategies

pip install matplotlib'''

import matplotlib,pyplot as pit
x = [1,2,3,4,5]
y = [10,20,15,25]
pip.plot(x,y)
pit.show()
