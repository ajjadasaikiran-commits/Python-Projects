# ==========================
# RESTAURANT ORDER SYSTEM
# ==========================

# 1. View Menu
# 2. Order Food
# 3. View Cart
# 4. Remove Item
# 5. Generate Bill
# 6. Exit

#........................................................................................
menu = {}
cart = {}
while True:
    print("\n1.Add Items(Owner)\n2.View Menu\n3.Order Food\n4.View Cart\n5.Remove Item\n6.Generate Bill\n7.Exit\n")
    option = int(input("Enter Option:"))
    if option == 1:
        name = input("Enter Item Name:")
        price = int(input("Enter Price:"))
        menu[name] = price
        print("Item Added Sucessfully")
    elif option == 2:
        print("\n===================")
        print("         menu")
        for item in menu:
            print(item, "₹",menu[item])
        print("===================")
    elif option == 3:
        foodname = input("Enter Food Name:")
        quantity = int(input("Enter Quantity:"))
        if foodname in menu:
            cart[foodname]=quantity
        else:
            print("Item is Not in Menu")
    elif option == 4:
        print("\n===================")
        print("         cart")
        for item in cart:
            print(item , "₹",cart[item]*menu[item])
        print("===================")
    elif option == 5:
        removename = input("Enter Item Name To Remove:")
        if removename in cart:
            del cart[removename]
        else:
            print("Name is Not Found in Cart to Remove")
    elif option == 6:
        print("========================")
        print("         BILL")
        print("========================")
        if not cart:
            print("No Item in Cart No Bill")
        else:
            total =0
            for item in cart:
                print(item," ",cart[item],"x",menu[item])
                total = total + cart[item]*menu[item]
            print("Subtotal:",total)
            print("GST (5%):",total* 5 / 100)
            print("Total Amount:",total + total*(1 + 5/100))
    elif option == 7:
        print("\nHave a NiceDay\nComeBack and Vist again To GET Discount")
        break
    else:
        print("Invalid Option..")
print("Program Completed")



