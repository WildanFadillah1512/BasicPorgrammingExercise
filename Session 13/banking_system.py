from Account import Account

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            return False  # Account number already exists
        self.accounts[account_number] = Account(account_number, account_holder)
        return True

    def deposit_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        return False  # Account number does not exist

    def withdraw_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False  # Account number does not exist

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        return None  # Account number does not exist
