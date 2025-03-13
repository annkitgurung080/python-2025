# books=['python','javascript','php']
# users=[
#     {'username':'ram','password':'ram002'}
#     {'username':'hari','password':'hari002'}
# ]
username=(input("Enter your username: "))
if username =='ram' or username=='hari':
    password=(input("Enter your Password: "))
    if password=='hari002'or password=='ram002':
        print("You are logged in ")
        print("Welcome to E-Books")
        print("Choose Your Books:")
        books=int(input("1. Python  2. Javascript  3.Php ::"))  
        if books==1:
            print("You are accesed to Python Book")      
        elif books==2:
            print("You are accesed to Javascript Book")    
        elif books==3:
            print("You are accesed to Php Book")    
        else:
            print("Ivalid option !!!")
            exit()
    else:
        print("Invalid Password !!")
        exit()
else:
    print("Invalid Username !!")
    exit()