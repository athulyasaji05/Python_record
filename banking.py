class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest added to account {self.account_number}. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def display_balance(self):
        print(f"Current Account {self.account_number} balance: {self.balance}")

# Example usage:
def main():
    # Creating savings account
    savings_acc = SavingsAccount("SAV123", 5000, 0.02)
    savings_acc.display_balance()
    savings_acc.deposit(2000)
    savings_acc.add_interest()
    savings_acc.withdraw(1500)
    savings_acc.display_balance()

    # Creating current account
    current_acc = CurrentAccount("CUR456", 10000, 2000)
    current_acc.display_balance()
    current_acc.deposit(3000)
    current_acc.withdraw(12000)
    current_acc.display_balance()

if __name__ == "__main__":
    main()
