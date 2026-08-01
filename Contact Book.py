#.........................................................................................
# Contact Book
# Without loops.
# Menu
# 1 Add Contact
# 2 View Contact
# 3 Delete Contact
# Use a dictionary.
# Example
# {
# "Sai":"9876543210",
# "Rahul":"9999999999"
# }
# Based on the user's choice:
# Add a contact
# View a contact
# Delete a contact
# Use only if, elif, and dictionary methods.
#........................................................................................

book = {}
print("Contact Book")
while True:
    option = int(input("1.Add Contact\n2.View Contact\n3.Delete Contact\n4.Exit Book\n"))
    if(option == 1):
        name = input("Enter Name:")
        num = int(input("Enter Phone Number:"))
        book[name]=num
        print("Contact Saved Scuessfully")
    elif(option == 2):
        if not book:        #check Dict Empty or not
            print("Contact Book is Empty")
        else:
            name = input("Enter Name To View:")
            if name in book: #checking key in Dict
                print("Contact Number:",book[name])
            else:
                print("Contact is Not Found")
    elif( option == 3):
        if not book:
            print("Contact Book is Empty")
        else:
            name = input("Enter Name To View:")
            if name in book:
                del book[name] # delete pair in dict
                print("Contact Deleted Sucessfully")
            else:
                print("Contact Not Found")
    elif( option == 4):
        print("Book is Closing Bye")
        break # break the loop block
    else:
        print("Invalid Option")
print("Book is Closeing Bye")          
