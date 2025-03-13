print("-----------ATM------------")
pin=int(input("Enter your pin :"))
if pin == 1004:
    print("Welcome to ATM")
    print("Enter your option ")
    print("1. Check Balance ")
    print("2. Winthdraw Amount")
    amount=100000
    option=int(input("Enter your option:"))
    if option==1:
        print("Your Balance is:",amount)
    elif option==2:
        new_amount=int(input("Enter the amount to withdraw: "))
        if amount>=new_amount:
            re_amount=amount-new_amount
            print("Your new balance is :",re_amount)
            print("Withdraw amount: ", new_amount)
        else:
            print("Insufficient balance")
            exit()
    else:
        print("Invalid option")
        exit()
else:
    print("Invalid pin")
    exit()
    
