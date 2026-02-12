# Bank Management System

def create_account():
    name = input("Enter account holder name: ")
    acc_no = int(input("Enter account number: "))
    balance = float(input("Enter initial balance: "))

    account = {
        "name": name,
        "acc_no": acc_no,
        "balance": balance
    }

    print("Account created successfully!\n")
    return account


def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount deposited successfully!")
    print("Updated Balance:", account["balance"], "\n")


def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")
    print("Current Balance:", account["balance"], "\n")


def check_balance(account):
    print("\n----- Account Details -----")
    print("Name:", account["name"])
    print("Account Number:", account["acc_no"])
    print("Balance:", account["balance"])
    print("---------------------------\n")


def main():
    account = None

    while True:
        print("====== BANK MENU ======")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = create_account()

        elif choice == "2":
            if account:
                deposit(account)
            else:
                print("Please create an account first!\n")

        elif choice == "3":
            if account:
                withdraw(account)
            else:
                print("Please create an account first!\n")

        elif choice == "4":
            if account:
                check_balance(account)
            else:
                print("Please create an account first!\n")

        elif choice == "5":
            print("Thank you for using the Bank System!")
            break

        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
#OUTPUT
====== BANK MENU ======
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
Enter your choice: 1

Enter account holder name: John
Enter account number: 101
Enter initial balance: 5000
Account created successfully!

====== BANK MENU ======
Enter your choice: 2
Enter amount to deposit: 2000
Amount deposited successfully!
Updated Balance: 7000.0

====== BANK MENU ======
Enter your choice: 3
Enter amount to withdraw: 1000
Withdrawal successful!
Current Balance: 6000.0

====== BANK MENU ======
Enter your choice: 4

----- Account Details -----
Name: John
Account Number: 101
Balance: 6000.0
---------------------------

====== BANK MENU ======
Enter your choice: 5
Thank you for using the Bank System!
