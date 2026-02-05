#_________Basic Structure
class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

obj=Child()
obj.show()

k=Parent()
k.show()

#____________With Overriding
class Animal:
    def speak(self):
        print("Some sound.")

class Dog(Animal):
    def speak(self):
        print("Bark")

a=Animal()
d=Dog()

a.speak()
d.speak()

#________Super() to access parent method
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d=Dog()
d.speak()

#_____________overriding
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def start(self):
        print("Car started.")

c=Car()
c.start()

