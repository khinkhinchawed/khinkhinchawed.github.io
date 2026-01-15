rice1=7000
rice2=8000
oil1=12000
oil2=13000
salt1=1500
salt2=2000
print("Welcome to my shop!What do you want?")
print("Rice for 1,Oil for 2,Salt for 3,none for 0")
userInput=input("Enter your choice:")

if userInput == "1":#---------rice
    category=int(input("1 for rice1(7000),2 for rice(8000)and  none for 0"))
    if category == 0:
        print("Exit")
    if category==1:#7000 for pyi and pone
        measure=int(input("Do you want to buy Pyi Or Pone:"))
        if measure==1:
          rice_amount=int(input("Enter your rice amount:"))
          price=rice_amount*rice1
          print(f"Total price is {price} kyats.")

        if measure == 2:
            rice_amount = int(input("Enter your rice amount:"))
            price = (rice_amount/8) * rice1
            print(f"Total price is {price} kyats.")
    elif category == 2:#8000 for pyi and pone
        measure = int(input("Do you want to buy Pyi Or Pone:"))
        if measure==1:
            rice_amount=int(input("Enter your rice amount:"))
            price=rice_amount*rice2
            print(f"Total price is {price} kyats.")

        if measure == 2:
            rice_amount = int(input("Enter your rice amount:"))
            price = (rice_amount/8) * rice2
            print(f"Total price is {price} kyats.")



elif userInput == "2":#-----------Oil1 for kg and L
    category=int(input("1 for oi1(12000),2 for oil2(13000)and  none for 0"))
    if category == 0:
        print("Exit")
    if category==1:
        measure=int(input("Do you want to buy kg or L:"))
        if measure==1:
          oil=int(input("Enter the amount of oil:"))
          price=oil*oil1/0.9
          print(f"Total price is {price} kyats.")

        if measure == 2:
            oil = int(input("Enter the amount of oil:"))
            price = (oil*0.9)*oil1
            print(f"Total price is {price} kyats.")

    if category==2:#Oil2 for kg and l
        measure = int(input("Do you want to buy kg or L:"))
        if measure==1:
            oil=int(input("Enter the  amount of oil:"))
            price =( oil * oil2) / 0.9
            print(f"Total price is {price} kyats.")

        if measure == 2:
            oil= int(input("Enter the  amount of oil :"))
            price = (oil * 0.9) * oil2
            print(f"Total price is {price} kyats.")

elif userInput == "3":#Salt1 for kg,gram
    category=int(input("1 for salt1(1500),2 for salt2(2000)and  none for 0"))
    if category == 0:
        print("Exit")
    if category==1:
        measure=int(input("Do you want to buy kg or gram:"))
        if measure==1:
          salt=int(input("Enter your amount of salt:"))
          price=salt1*salt
          print(f"Total price is {price} kyats.")

        if measure == 2:
            salt = int(input("Enter the amount of salt:"))
            price = (salt1*salt)/1000
            print(f"Total price is {price} kyats.")

    if category==2:#Salt2 for kg and g
        measure = int(input("Do you want to buy kg or gram:"))
        if measure==1:
          salt=int(input("Enter the amount of salt::"))
          price = salt2 * salt
          print(f"Total price is {price} kyats.")


        if measure == 2:
            salt= int(input("Enter the  amount of salt::"))
            price = (salt1 * salt) / 1000
            print(f"Total price is {price} kyats.")

elif userInput == "0":
    print("Goodbye.See you next time!")

else:
    print("Goodbye.See you next time!")
