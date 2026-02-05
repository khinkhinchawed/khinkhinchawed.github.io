class BankAccount:
    def __init__(self,name,pin,balance=0):
        self.__name=name
        self.__pin=pin
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(amount, "deposited successfully.")

        else:
            print("Invalid deposit amount.")

B=BankAccount("kkc","123",1000)
print(B.deposit(1000))
print(B.deposit(00))
