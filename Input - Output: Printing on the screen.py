# Supermarket Billing System

print("=========== WELCOME TO ABC SUPERMARKET ===========")

# Customer Details
customer_name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")

print("\nEnter details of 3 items:")

# Item 1
item1 = input("Item 1 name: ")
price1 = float(input("Item 1 price: "))
qty1 = int(input("Item 1 quantity: "))

# Item 2
item2 = input("\nItem 2 name: ")
price2 = float(input("Item 2 price: "))
qty2 = int(input("Item 2 quantity: "))

# Item 3
item3 = input("\nItem 3 name: ")
price3 = float(input("Item 3 price: "))
qty3 = int(input("Item 3 quantity: "))

# Calculations
total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3

subtotal = total1 + total2 + total3
tax = subtotal * 0.05
grand_total = subtotal + tax

# Printing Bill
print("\n\n================= BILL =================")
print(f"Customer Name : {customer_name}")
print(f"Mobile No     : {mobile}")
print("----------------------------------------")
print("Item\t\tQty\tPrice\tTotal")
print("----------------------------------------")

print(f"{item1}\t\t{qty1}\t{price1}\t{total1}")
print(f"{item2}\t\t{qty2}\t{price2}\t{total2}")
print(f"{item3}\t\t{qty3}\t{price3}\t{total3}")

print("----------------------------------------")
print(f"Subtotal : {subtotal}")
print(f"Tax (5%) : {tax}")
print(f"Grand Total : {grand_total}")
print("========================================")
print("        THANK YOU! VISIT AGAIN         ")
#OUTPUT
=========== WELCOME TO ABC SUPERMARKET ===========
Enter customer name: Ramesh
Enter mobile number: 9876543210

Enter details of 3 items:
Item 1 name: Rice
Item 1 price: 50
Item 1 quantity: 2

Item 2 name: Oil
Item 2 price: 120
Item 2 quantity: 1

Item 3 name: Sugar
Item 3 price: 40
Item 3 quantity: 3


================= BILL =================
Customer Name : Ramesh
Mobile No     : 9876543210
----------------------------------------
Item            Qty     Price   Total
----------------------------------------
Rice            2       50.0    100.0
Oil             1       120.0   120.0
Sugar           3       40.0    120.0
----------------------------------------
Subtotal : 340.0
Tax (5%) : 17.0
Grand Total : 357.0
========================================
        THANK YOU! VISIT AGAIN
