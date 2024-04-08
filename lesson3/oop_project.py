from bank_accounts import *

Emma = BankAccount(1000, "Emma")
John = BankAccount(500, "John")

Emma.getBalance()
John.getBalance()

# Emma.deposit(500)

Emma.withdraw(18000)
Emma.deposit(11000)
Emma.transfer(1500, John)

Grace = InterestRewardAcct(2000, "Grace")

Grace.getBalance()

Grace.deposit(100)

Emma.transfer(2500, Grace)
 
GraceLoan = InterestAccount(5000, "GraceLoan", 0.05)

Grace.getBalance()

GraceLoan.addInterest()


Adamu = SavingsAccount(1000, "Adamu")

Adamu.getBalance()

Adamu.deposit(500)

Adamu.transfer(20000, Emma)
Adamu.transfer(1000, Emma)

