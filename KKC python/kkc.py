inventory={}
while True:
    print("\n1.Add Item.")
    print("2.Update Quality")
    print("3.View Inventory")
    print("4.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
       name=input("Enter your input:")
       qty=input("Enter your quality:")
       inventory[name]=qty
       print(f"Added item with {name}with{qty}")

    elif choice == '2':
        item = input("Enter item name: ")
        if item in inventory:
           qty = (input("Enter new quantity: "))
           inventory[item] = qty
           print(f"Updated {item}'s quantity to {qty}.")
        else:
             print("Item not found.")


    elif choice=="3":
        if not inventory:
            print("Empty.")
        else:
            for name,qty in inventory.items():
                print(f"{name}:{qty}")

    elif choice=="4":
        break
    else:
     print("Invalid choice:")
            
          
        


    


