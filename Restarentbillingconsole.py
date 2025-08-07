print("#### Restaurant Billing System ####\n")

# List to store order records
order_list = []

while True:
    print("""
Choose:
    1. Add New Order
    2. Remove Order
    3. Show All Orders
    4. Exit
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Add New Order ---")
        order_id = input("Enter Order ID: ")
        customer_name = input("Enter Customer Name: ")

        items = []
        total = 0

        while True:
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price per Item: "))
            amount = quantity * price

            items.append({
                "Item": item_name,
                "Quantity": quantity,
                "Price": price,
                "Amount": round(amount, 2)
            })

            total += amount

            more = input("Add more items? (y/n): ")
            if more.lower() != 'y':
                break

        tax = total * 0.05  # 5% tax
        grand_total = total + tax

        order = {
            "Order ID": order_id,
            "Customer Name": customer_name,
            "Items": items,
            "Total": round(total, 2),
            "Tax (5%)": round(tax, 2),
            "Grand Total": round(grand_total, 2)
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
            print("Order not found.\n")

    elif choice == 3:
        print("\n--- All Orders ---")
        if not order_list:
            print("No orders found.\n")
        else:
            for i, order in enumerate(order_list, 1):
                print(f"\nOrder {i}")
                print("Order ID:", order["Order ID"])
                print("Customer Name:", order["Customer Name"])
                print("Items:")
                for item in order["Items"]:
                    print(f"  - {item['Item']} | Qty: {item['Quantity']} | Price: {item['Price']} | Amount: {item['Amount']}")
                print("Total:", order["Total"])
                print("Tax (5%):", order["Tax (5%)"])
                print("Grand Total:", order["Grand Total"])
                print("-" * 30)

    elif choice == 4:
        print("Thanks for using Restarent billing system")
