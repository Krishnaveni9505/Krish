print("#### Student Details System ####")
print()

# Initializing storage for student records
student_list = []

while True:
    print("""
Choose:
    1. Add Student Details
    2. Remove Student Details
    3. Show All Student Details
    4. Exit
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Add Student ---")
        name = input("Enter the Name: ")
        roll_num = input("Enter the Roll Number: ")
        branch = input("Enter the Branch: ")
        section = input("Enter the Section: ")
        ph_num = input("Enter the Phone Number: ")
        email = input("Enter the Email: ")
        dept = input("Enter the Department: ")

        java_marks = int(input("Enter Java Marks: "))
        python_marks = int(input("Enter Python Marks: "))
        dn_marks = int(input("Enter DotNet Marks: "))
        db_marks = int(input("Enter Database Marks: "))
        wd_marks = int(input("Enter Web Development Marks: "))

        # Calculate total, average and grade
        total = java_marks + python_marks + dn_marks + db_marks + wd_marks
        average = total / 5

        # Grade logic
        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        else:
            grade = 'Fail'

        student = {
            "Name": name,
            "Roll Number": roll_num,
            "Branch": branch,
            "Section": section,
            "Phone": ph_num,
            "Email": email,
            "Department": dept,
            "Java": java_marks,
            "Python": python_marks,
            "DotNet": dn_marks,
            "Database": db_marks,
            "Web Development": wd_marks,
            "Total Marks": total,
            "Average": average,
            "Grade": grade
        }

        student_list.append(student)
        print("Student added successfully!\n")

    elif choice == 2:
        print("\n--- Remove Student ---")
        roll_num = input("Enter the Roll Number of the student to remove: ")
        removed = False
        for student in student_list:
            if student["Roll Number"] == roll_num:
                student_list.remove(student)
                print("Student removed successfully!\n")
                removed = True
                break
        if not removed:
            print("Student not found.\n")

    elif choice == 3:
        print("\n--- All Student Details ---")
        if not student_list:
            print("No student records found.\n")
        else:
            for i, student in enumerate(student_list, 1):
                print("Student", i)
                print("Name:", student["Name"])
                print("Roll Number:", student["Roll Number"])
                print("Branch:", student["Branch"])
                print("Section:", student["Section"])
                print("Phone:", student["Phone"])
                print("Email:", student["Email"])
                print("Department:", student["Department"])
                print("Java Marks:", student["Java"])
                print("Python Marks:", student["Python"])
                print("DotNet Marks:", student["DotNet"])
                print("Database Marks:", student["Database"])
                print("Web Development Marks:", student["Web Development"])
                print("Total Marks:", student["Total Marks"])
                print("Average:", student["Average"])
                print("Grade:", student["Grade"])
                if student["Grade"] == "Fail":
                    print("Result: Better luck next time")
                else:
                    print("Result: Passed")
                print("--------------------------")



    elif choice == 4:
        print("Thanks for using Student Details System.")