print("#### Restaurant Billing System ####\n")

# List to store all restaurant orders
order_list = []

while True:
    print("""
Choose:
    1. Add New Order
    2. Remove Order
    3. View All Orders
    4. Search Order by Table Number
    5. Edit Order
    6. Exit
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Add New Order ---")
        order_id = input("Enter Order ID: ")
        table_number = input("Enter Table Number: ")
        customer_name = input("Enter Customer Name: ")

        items = []
        subtotal = 0

        while True:
            item_name = input("Enter Food Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price per Unit: "))
            amount = quantity * price

            items.append({
                "Food Item": item_name,
                "Quantity": quantity,
                "Price": price,
                "Amount": round(amount, 2)
            })

            subtotal += amount

            more = input("Add more food items? (y/n): ")
            if more.lower() != 'y':
                break

        service_charge = subtotal * 0.10  # 10% service charge
        total_amount = subtotal + service_charge

        order = {
            "Order ID": order_id,
            "Table Number": table_number,
            "Customer Name": customer_name,
            "Items": items,
            "Subtotal": round(subtotal, 2),
            "Service Charge (10%)": round(service_charge, 2),
            "Total Amount": round(total_amount, 2)
        }

        order_list.append(order)
        print("Order added successfully!\n")

    elif choice == 2:
        print("\n--- Remove Order ---")
        order_id = input("Enter the Order ID to remove: ")
        removed = False
        for order in order_list:
            if order["Order ID"] == order_id:
                order_list.remove(order)
                print("Order removed successfully!\n")
                removed = True
                break
        if not removed:
            print("Order ID not found.\n")

    elif choice == 3:
        print("\n--- All Orders ---")
        if not order_list:
            print("No orders found.\n")
        else:
            for i, order in enumerate(order_list, 1):
                print(f"\nOrder {i}")
                print("Order ID:", order["Order ID"])
                print("Table Number:", order["Table Number"])
                print("Customer Name:", order["Customer Name"])
                print("Items:")
                for item in order["Items"]:
                    print(f"  - {item['Food Item']} | Qty: {item['Quantity']} | Price: {item['Price']} | Amount: {item['Amount']}")
                print("Subtotal:", order["Subtotal"])
                print("Service Charge (10%):", order["Service Charge (10%)"])
                print("Total Amount:", order["Total Amount"])
                print("-" * 30)

    elif choice == 4:
        print("\n--- Search Order by Table Number ---")
        table_number = input("Enter Table Number to search: ")
        found = False
        for order in order_list:
            if order["Table Number"] == table_number:
                print("Order ID:", order["Order ID"])
                print("Customer Name:", order["Customer Name"])
                print("Items:")
                for item in order["Items"]:
                    print(f"  - {item['Food Item']} | Qty: {item['Quantity']} | Price: {item['Price']} | Amount: {item['Amount']}")
                print("Subtotal:", order["Subtotal"])
                print("Service Charge (10%):", order["Service Charge (10%)"])
                print("Total Amount:", order["Total Amount"])
                print("-" * 30)
                found = True
        if not found:
            print("No orders found for this table.\n")

    elif choice == 5:
        print("\n--- Edit Order ---")
        order_id = input("Enter Order ID to edit: ")
        for order in order_list:
            if order["Order ID"] == order_id:
                print("Editing order for:", order["Customer Name"])
                customer_name = input("Enter new Customer Name (leave blank to keep current): ")
                table_number = input("Enter new Table Number (leave blank to keep current): ")

                if customer_name:
                    order["Customer Name"] = customer_name
                if table_number:
                    order["Table Number"] = table_number

                print("Re-enter food item details:")
                items = []
                subtotal = 0
                while True:
                    item_name = input("Enter Food Item Name: ")
                    quantity = int(input("Enter Quantity: "))
                    price = float(input("Enter Price per Unit: "))
                    amount = quantity * price

                    items.append({
                        "Food Item": item_name,
                        "Quantity": quantity,
                        "Price": price,
                        "Amount": round(amount, 2)
                    })

                    subtotal += amount

                    more = input("Add more food items? (y/n): ")
                    if more.lower() != 'y':
                        break

                service_charge = subtotal * 0.10
                total_amount = subtotal + service_charge

                order["Items"] = items
                order["Subtotal"] = round(subtotal, 2)
                order["Service Charge (10%)"] = round(service_charge, 2)
                order["Total Amount"] = round(total_amount, 2)

                print("Order updated successfully!\n")
                break
        else:
            print("Order ID not found.\n")

    elif choice == 6:
        print("Thanks for using Restaurant Billing System.")
        break

    else:
        print("Invalid choice. Please try again.\n")
