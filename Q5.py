


class Account():

    def __init__(self, account_holder_name: str, initial_balance: float, percentage_interest_rate: float):
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
        self.interest_rate = percentage_interest_rate
        init_msg = f"The name of the account holder is {self.account_holder_name}"
        init_msg += f"\nThe initial balance of the account is ${round(self.balance, 2): .2f}"
        print(init_msg)

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"After depositing ${round(amount, 2): .2f}, the balance is ${round(self.balance, 2): .2f}")

    def withdraw(self, amount: float) -> float:
        if amount < self.balance:
            out = self.balance - amount 
            self.balance -= amount
            print("After withdrawing", end=' ')
        else:
            out = 0.00
            print("After trying to withdraw", end=' ')
        print(f"${round(amount, 2): .2f}, the balance is ${round(self.balance, 2): .2f}")
        return out

    def apply_interest(self):
        self.balance *= self.interest_rate
        print(f"Interest rate of {self.interest_rate: .2f}% applied, the balance is now {self.balance}")
        

    def __str__(self):
        out =  f"Account name: {self.account_holder_name}"
        out += f"\nBalance: ${round(self.balance, 2): .2f}"
        return out
    

def testAccount():
    matsAccount = Account("Matthew Poole", 0, 0)
    matsAccount.deposit(100)
    matsAccount.withdraw(50)
    matsAccount.withdraw(100)
    print(matsAccount)

# testAccount()
