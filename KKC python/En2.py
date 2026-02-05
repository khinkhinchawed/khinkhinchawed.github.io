class Student:
    def __init__(self,name):
        self.__name=name

    @property 
    def name(self):#acts like a getter
       return self.__name

    @name.setter
    def name(self,value):
         self.__name=value
    
S=Student("Alice")
print(S.name)
S.name="Bob"
print(S.name)

class Product:
    def __init__(self,price):
        self.__price=price

    @property
    def price(self):#getter
        return self.__price
    
    @price.setter
    def price(self,value):
        if value>0:
            self.__price=value
        else:
            print("Price must be positive.")

p=Product(100)
print(p.price)
p.price=150
print(p.price)
p.price=-50