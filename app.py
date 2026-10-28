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

def main():
    account = BankingSystem(100.0)
    print("--- Welcome to the Banking App (v1.0) ---")
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            print(f"Current Balance: ${account.check_balance():.2f}")
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
            print("Deposit successful!")
        elif choice == "3":
            break
