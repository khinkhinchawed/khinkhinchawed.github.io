class Person:            #build class firstly
    def __init__(self,name,age):#as definite
        self.__name=name #private
        self.__age=age #private

    def get_name(self):   #function1
        return self.__name
    
    
    
    def set_age(self,age):  #function2
        if age>0:
            self.__age=age
        else:
            print("Age must be positive.") 

    def get_age(self):
        return self.__age

p=Person("Alice",25)  # call class and insert value into parameter

print(p.get_name()) #call function1 inside class
print(p.get_age())

p.set_age(-5)
print(p.get_age())

class Student:
    def __init__(self,name):
        self.__name=name
    #getter method
    def get_name(self):
        return self.__name
    #Setter method
    def set_name(self,new_name):
        self.__name=new_name

S=Student("Khin")
print(S.get_name())

S.set_name("chaw")
print(S.get_name())

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
           self.__name=name

    def get_salary(self):
        return self.__salary
    
E=Employee("KKC",1500000)
print(E.get_name())

E.set_name("CKk")
print(E.get_name())

print(E.get_salary())




    

    









