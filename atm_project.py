icici_hemateja_ac_details = {"Name":"Kosana Hema Teja Reddy",
                            "date-of-brith" : "10-09-2004",
                            "ATM PIN" : "934728",
                            "Balance" : 20000}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_hemateja_ac_details['ATM PIN']:
        icici_user_choice = int(input("enter \n1.withdraw: \n2:deposite: ")) 
        if icici_user_choice == 1:
            money_w = int(input("enter the money to withdraw : "))
            if money_w <= icici_hemateja_ac_details['Balance']:
                icici_hemateja_ac_details['Balance'] -= money_w
                print(icici_hemateja_ac_details['Balance'])
            else:
                print("insuff")
        elif user_choice == 2:
            deposite_m = int(input("pls enter the money you want to deposite: "))
            if deposite_m % 100 == 0 and deposite_m >= 5000:
                icici_hemateja_ac_details['Balance'] += deposite_m
                print(f"you have deposite {deposite_m} and total is {icici_hemateja_ac_details['Balance']}")
            else :
                print(f"{deposite_m} you have entered is change or less than {5000}")
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")
