class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully. Remaining balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, recipient_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} to {recipient_account.account_holder} successfully.")
            print(f"Your new balance: {self.balance}")
        else:
            print("Invalid transfer amount or insufficient funds.")

# Example usage
def main():
    account1 = BankAccount("12345", "Alice", 1000)
    account2 = BankAccount("67890", "Bob", 500)

    print("Initial Balances:")
    print(f"{account1.account_holder}: {account1.balance}")
    print(f"{account2.account_holder}: {account2.balance}\n")

    # Perform a transfer
    account1.transfer(account2, 200)

    print("\nBalances after transfer:")
    print(f"{account1.account_holder}: {account1.balance}")
    print(f"{account2.account_holder}: {account2.balance}")

if __name__ == "__main__":
    main()
