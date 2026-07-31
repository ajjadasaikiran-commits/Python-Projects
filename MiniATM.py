# Mini ATM Login.......................................................................................................................
# Store:
# username = "admin"
# password = "Python@123"
# balance = 5000
# Take input:
# Username
# Password
username = input("Enter UserName:")
password = input("Enter Password:")
balance = 5000
if(username == "admin" and password == "Python@123456"):
    print("login Scuesses")
    option = int(input("Operations:\n1.Deposit\n2.Withdraw\n3.Exit\n"))
    while(option != 3):
        if(option == 1):
            deposit = int(input("Enter Amount to Deposit:")) 
            balance = balance+deposit
            print("Total Amount in Account:",balance)
        elif(option == 2):
            withdraw = int(input("Enter Amount to WithDraw:"))
            balance = balance-withdraw
            if(balance >= 0):
                print("Total Amount in Account:",balance)
            else:
                print("Insufficient balance")
        else:
            print("Invalid Option...")
        option = int(input("Operations:\n1.Deposit\n2.Withdraw\n3.Exit\n"))
    print("Welcome Back Bye User")
else:
    print("Invalid Details\tLogin Failed")
#.........................................................................................................................................