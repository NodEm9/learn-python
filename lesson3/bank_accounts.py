class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\nAccount for {self.acctName} created with initial balance of: \nOpen amount: ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nCurrent balance for account {self.acctName} is ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nAmount: ${amount:.2f} deposited into account {self.acctName}. \nNew balance is ${self.balance:.2f}")
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nInsufficient funds for transaction. \nCurrent balance: ${self.balance:.2f}")
    
    def withdraw(self, amount):
     try:
        self.viableTransaction(amount)
        self.balance -= amount
        print(f"\nAmount: ${amount:.2f} withdrawn from account {self.acctName}. \nNew balance is ${self.balance:.2f}")
     except BalanceException as e:
        print(f"\n Withdraw was interrupted: {e}")
    
    def transfer(self, amount, recipient):
        try:
            print('\n*********************\n\nTransfer initiated..🚀')
            self.viableTransaction(amount)
            self.balance -= amount
            recipient.balance += amount
            print(f"\nAmount: ${amount:.2f} transferred to account {recipient.acctName}. \nNew balance for {self.acctName} is ${self.balance:.2f}")
            print('\n****\n\nTransfer completed..✅ 🎉')
            print(f"\nNew balance for: {recipient.acctName} is ${recipient.balance:.2f}")
        except BalanceException as e:
            print(f"\n Transfer was interrupted: ❌ {e}")


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class InterestAccount(BankAccount):
    def __init__(self, initialAmount, acctName, interestRate):
        super().__init__(initialAmount, acctName)
        self.interestRate = interestRate

    def addInterest(self):
        interest = self.balance * self.interestRate
        self.balance += interest
        print(f"\nInterest of ${interest:.2f} added to account {self.acctName}. \nNew balance is ${self.balance:.2f}")
        self.getBalance()


class SavingsAccount(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.interestRate = 0.05

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.interestRate)
            self.balance -= (amount + self.interestRate)
            print(f"\nAmount: ${amount:.2f} withdrawn from account {self.acctName}. \nNew balance is ${self.balance:.2f}")
            print("\nWithdrawal fee of $5 has been deducted from your account.")
            print("\nWithdrawal Completed.") 
            self.getBalance()
        except BalanceException as e:
            print(f"\n Withdraw was interrupted: {e}")
          