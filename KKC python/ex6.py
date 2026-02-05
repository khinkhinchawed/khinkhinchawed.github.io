print("Functional Requirement")
List1=[]
while True:
    print("1.Insert Task.")
    print("2.View Task.")
    print("3.Update Task.")
    print("4.Delete Task.")
    print("5.Exit Program.")

    choice=input("Enter your choice:")
    if choice == "1":
        new_task=input("Enter the new task:")
        List1.append(new_task)
    
    elif choice=="2":
        if not List1:
            print("Not found.")

        else:
            for new_task in List1:
                print("The result is:",new_task)

    elif choice=="3":
        
            ID=int(input("Enter the ID you want to change:"))
            test=input("Enter your new function:")
            List1[ID]=test
            for ID in List1:
                print("The update is successful.")


                    
        
