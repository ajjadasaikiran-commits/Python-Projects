# Mini Project: Inventory Management System
# Menu
# ==============================
#    INVENTORY MANAGEMENT
# ==============================
# 1. View Products
# 2. Add Product
# 3. Search Product
# 4. Update Product Quantity
# 5. Delete Product
# 6. Total Products
# 7. Exit

print("===========================")
print("    INVENTORY MANAGEMENT")
print("===========================")
dict = {}
while True:
    option = int(input("1. View Products\n2. Add Product\n3. Search Product\n4. Update Product Quantity\n5. Delete Product\n6. Total Products\n7. Exit\n"))
    if option == 1:
        if not dict:
            print("System is Empty")
        else:
            print(dict)
    elif option == 2:
        name = input("Enter Product Name:")
        quan = int(input("Enter Quantity:"))
        dict[name]= quan
        print("Add SucessFully")
    elif option == 3:
        if not dict:
            print("System is Empty")
        else:
            name = input("Enter Product Name To Search:")
            if name in dict:
                print(name,"Quantity is",dict[name])
            else:
                print("Invalid Product Name...")
    elif option == 4:
        if not dict:
            print("System is Empty")
        else:
            name = input("Enter Product Name to Update:")
            if name in dict:
                num = int(input("Enter Quantity:"))
                dict[name]=num
                print("Updated Sucessfully")
            else:
                print("Invalid Product Name...")
    elif option == 5:
        if not dict:
            print("System is Empty")
        else:
            name = input("Enter Product Name to Deleted:")
            if name in dict:
                del dict[name]
                print("Deleted Sucessfully")
    elif option == 6:
        if not dict:
            print("System is Empty")
        else:
            print("Total Number Products is:",len(dict))
    elif option == 7:
        print("System is Exiting Bye !")
        break
    else:
        print("Invalid Option ReEnter Option:")
