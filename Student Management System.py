# Mini project Project Menu
# =================================
#       STUDENT MANAGEMENT
# =================================

# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update Student Marks
# 5. Delete Student
# 6. Show Topper
# 7. Show Class Average
# 8. Show Passed Students
# 9. Show Failed Students
# 10. Exit
#..................................................................................................................

students =[]

while True:
    print("1. Add Student\n2. View All Students\n3. Search Student\n4. Update Student Marks\n5. Delete Student\n6. Show Topper\n7. Show Class Average\n8. Show Passed Students\n9.Show Failed Students\n10. Exit")
    option = int(input("Enter Option:"))
    found = False
    if option == 1:
        rollno = input("Enter Roll Number:")
        for std in students:
            if std["Roll No"] == rollno:
                found = True
        if found == True:
            print("Already Exist")
            break
        else:
            newdict = {}
            markdist = {}
            name = input("Enter Student Name:")
            age = int(input("Enter Age:"))
            if age > 16:
                branch = input("Enter Branch:")
                marks = int(input("Enter Marks:"))
                newdict["Name"] = name
                newdict["Roll No"] = rollno
                newdict["Age"] = age
                newdict["Branch"] = branch
                markdist["Marks"] = marks
                newdict.update(markdist)
                students.append(newdict)
                print("Student Added Sucessfully")
            else:
                print("Age is Below 16")
    elif option == 2:
            if not students:
                print("No students In DataBase")
            else:
                for std in students:
                    print("Roll No :", std["Roll No"])
                    print("Name    :", std["Name"])
                    print("Age     :", std["Age"])
                    print("Branch  :", std["Branch"])
                    print("Marks   :", std["Marks"])
                    print("-" * 30)
    elif option == 3:
        if not students:
            print("No students In DataBase")
        else:
            rollno = input("Enter Roll Number:")
            for std in students:
                if std["Roll No"] == rollno:
                    print("Roll No :", std["Roll No"])
                    print("Name    :", std["Name"])
                    print("Age     :", std["Age"])
                    print("Branch  :", std["Branch"])
                    print("Marks   :", std["Marks"])
                    print("-" * 30)
            print("Searching Completed")
    elif option == 4:
        if not students:
            print("No students In DataBase")
        else:
            rollno = input("Enter Roll no to Update Marks:")
            for std in students:
                if std["Roll No"] == rollno:
                    marks = int(input("Enter Marks to Update:"))
                    markdist["Marks"] = marks
                    print("Marks Updated")
    elif option == 5:
        if not students:
            print("No students In DataBase")
        else:
            rollno = input("Enter Roll Number to Delete:")
            for std in students:
                if std["Roll No"] == rollno:
                    del std
                    print("Student Data Was Deleted")
    elif option == 6:
        if not students:
            print("No students In DataBase")
        else:
            topper = []
            high = 0
            for std in students:
                if markdist["Marks"] >= high:
                    high = markdist["Marks"]
                    topper.append(std["Name"])
            print("Topper's:",topper,"\nWith Marks:",high)
    elif option == 7:
        if not students:
            print("No students In DataBase")
        else:
            total = 0
            for std in students:
                total = total+markdist["Marks"]
            print("Class Average",total/(len(students)))
    elif option == 8:
        if not students:
            print("No students In DataBase")
        else:
            print("Passed Students:")
            for std in students:
                if markdist["Marks"] >= 35:
                    print(std["Name"])
    elif option == 9:
        if not students:
            print("No students In DataBase")
        else:
            print("Failed Students:")
            for std in students:
                if markdist["Marks"] <= 35:
                    print(std["Name"])
    elif option == 10:
        print("Exiting From The Student Data Base Bye Bye")
        break
print("Program is Complete ComeBack.")

#............................................................................................................................