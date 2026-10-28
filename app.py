class BankingSystem:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

def main():
    account = BankingSystem(100.0)
    print("--- Welcome to the Banking App (v2.0) ---")
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            print(f"Current Balance: ${account.check_balance():.2f}")
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            if account.deposit(amt):
                print("Deposit successful!")
            else:
                print("Invalid deposit amount.")
        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            if account.withdraw(amt):
                print("Withdrawal successful!")
            else:
                print("Transaction denied: Insufficient funds or invalid amount.")
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
