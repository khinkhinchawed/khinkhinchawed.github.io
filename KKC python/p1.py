class Parent:
    def speak(self):
        print("I am the parent.")

class Child(Parent):
    def greet(self):
        print("Hello from the child")
#---------------Single Inheritance
obj=Child()
obj.speak()
obj.greet()

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

dog=Dog()
dog.speak()
dog.bark()
#_________single inheritance

#-------------Multiple Inheritance
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps.")

p=Puppy()
p.bark()
p.speak()

#-------------Exercise
class Grandfather:
    def legacy(self):
        print("Legacy from Grandfather.")

class Father(Grandfather):
    def wisdom(self):
        print("Wisdom from father.")

class Son(Father):
    def energy(self):
        print("Energy from son.")

s=Son()
s.legacy()
s.wisdom()
s.energy()

#---------------Hierarchical inheritance
class Animal:
    def breathe(self):
        print("breathing....")
class Fish(Animal):
    def swim(self):
        print("Swimming....")

class Bird(Animal):
    def fly(self):
        print("Flying....")

f=Fish()
f.breathe()
f.swim()

b=Bird()
b.breathe()
b.fly()


#_____________Multiple Inheritance

class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A,B):
    def method_c(self):
        print("C")

obj=C()
obj.method_a()
obj.method_b()
obj.method_c()



#_________Exercise
class Father:
    def skills(self):
        print("Knows gardening")

class Mother:
    def skills(self):
        print("Knows cooking")

class Child(Father,Mother):
    pass

c=Child()
c.skills()



