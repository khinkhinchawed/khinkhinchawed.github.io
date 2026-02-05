class BankAccount:
    def interest_rate(self):
        print("Base interest rate:5%")

class SavingAccount(BankAccount):
    def interest_rate(self):
        print("Saving interest rate:7%.")



def display(account):
    account.interest_rate()

a=BankAccount()
s=SavingAccount()

display(a)
display(s)


