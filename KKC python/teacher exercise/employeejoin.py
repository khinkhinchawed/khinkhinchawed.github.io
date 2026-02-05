from employee1 import Employee
name=input("Enter your name:")
dept_name=input("Enter your dept")
salary=int(input("Enter the salary:"))
wh=int(input("Enter your salary"))

E2=Employee(name,dept_name,salary)

E2.calculate_salary(wh)
E2.show_info()