print("#### Employee Management System ####")
print()

# List to store employee records
employee_list = []

while True:
    print("""
Choose:
    1. Add Employee Details
    2. Remove Employee Details
    3. Show All Employee Details
    4. Exit
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Add Employee ---")
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        address = input("Enter Address: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        experience = input("Enter Experience: ")
        education = input("Enter Education: ")

        basic_salary = float(input("Enter Basic Salary: "))
        leaves_taken = int(input("Enter Leaves Taken: "))
        pt_amount = float(input("Enter PT (Professional Tax) Amount: "))

        # Salary Calculation
        per_day_salary = basic_salary / 30
        leave_deduction = leaves_taken * per_day_salary
        processed_salary = basic_salary - leave_deduction - pt_amount


        employee = {
            "Employee ID": emp_id,
            "Name": name,
            "Department": department,
            "Address": address,
            "Phone": phone,
            "Email": email,
            "Experience": experience,
            "Education": education,
            "Basic Salary": basic_salary,
            "Leaves Taken": leaves_taken,
            "PT Amount": pt_amount,
            "Processed Salary": round(processed_salary, 2)
        }

        employee_list.append(employee)
        print("Employee added successfully!\n")

    elif choice == 2:
        print("\n--- Remove Employee ---")
        emp_id = input("Enter the Employee ID to remove: ")
        removed = False
        for employee in employee_list:
            if employee["Employee ID"] == emp_id:
                employee_list.remove(employee)
                print("Employee removed successfully!\n")
                removed = True
                break
        if not removed:
            print("Employee not found.\n")

    elif choice == 3:
        print("\n--- All Employee Details ---")
        if not employee_list:
            print("No employee records found.\n")
        else:
            for i, employee in enumerate(employee_list, 1):
                print("Employee", i)
                print("Employee ID:", employee["Employee ID"])
                print("Name:", employee["Name"])
                print("Department:", employee["Department"])
                print("Address:", employee["Address"])
                print("Phone:", employee["Phone"])
                print("Email:", employee["Email"])
                print("Experience:", employee["Experience"])
                print("Education:", employee["Education"])
                print("Basic Salary:", employee["Basic Salary"])
                print("Leaves Taken:", employee["Leaves Taken"])
                print("PT Amount:", employee["PT Amount"])
                print("Processed Salary:", employee["Processed Salary"])
                print("--------------------------")

    elif choice == 4:
        print("Thanks for using Employee Management System.")

