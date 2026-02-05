class Employee:
    def __init__(self,name,dept_name,salary):
        self.name=name
        self.dept_name=dept_name
        self.salary=salary

    def calculate_salary(self,wh):
        self.wh=wh
        ot=wh-180
        self.salary+=ot*10

    def show_info(self):
        print(f"{self.name}is in the {self.dept_name}and {self.salary}.")


E1=Employee("KKC","Computer",1500000)
E1.show_info()