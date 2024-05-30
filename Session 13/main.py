from banking_system import BankingSystem

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def main():
    system = BankingSystem()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            if system.create_account(account_number, account_holder):
                print("Account created successfully.")
            else:
                print("Account number already exists.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = get_int_input("Enter amount to deposit: ")
            if system.deposit_money(account_number, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Account number does not exist or invalid amount.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = get_int_input("Enter amount to withdraw: ")
            if system.withdraw_money(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Account number does not exist or insufficient balance.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            balance = system.check_balance(account_number)
            if balance is not None:
                print(f"The balance for account {account_number} is {balance}.")
            else:
                print("Account number does not exist.")

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
