def withdraw(self,amount,pin):
    if pin==self.__pin:
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(str(amount)+"withdraw successfully.")

        else:
            print("Insufficient balance.")

    else:
        print("Incorrect PIN.Access denied.")