## Define the Account class and its attributes as specified above
class Account:
    def __init__(self, account_number, account_balance, acoount_holder, my_account) -> None:
        self.account_number = account_balance
        self.account_balance = account_balance
        self.account_holder = account_balance
        self.my_account = my_account

## Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
    def deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        print(f"Alert!!!{deposit_amount} has been added to your account")

## Define the check_balance() method. It should return the current account balance.
    def check_balance(self):
        print(f"Your current balance is {self.account_balance}")

    def withdrawal(self, withdrawal_amount):
        self.account_balance -= withdrawal_amount
        print(f"Your debit alart is {withdrawal_amount}")

account1 = Account("12345678", 200,000, "Kaybee", 30)
print(f"Good afternoon {account1.account_holder}, Your account balance is {account1.account_balance}")

## Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
account1.account_balance()
