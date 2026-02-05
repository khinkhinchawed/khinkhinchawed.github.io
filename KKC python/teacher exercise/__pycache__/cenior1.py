class Employee:
     def __init__(self,name,emp_id,dept_name):
          self.name=name
          self.emp_id=emp_id
          self.dept_name=dept_name

     def ShowEmployeeInfo(self):
          print(f"{self.name},{self.emp_id}and {self.dept_name}")

class Junior_Developer:
     def __init__(self,name,emp_id,dept_name,junior_basic_salary,working_hours):
          super().__init__(junior_basic_salary,working_hours)
          self.working_hours=working_hours
          self.junior_basic_salary=junior_basic_salary

      def Calculate_Junior_Salary(self,junior_basic_salary,working_hours):
          self.
          
          