Object-Oriented Programming (OOP) in Python
1️⃣ What is OOP?

Object-Oriented Programming is a programming style where programs are built using objects.

👉 Object = Data + Functions

2️⃣ Why OOP is Used?

OOP is used to:

Organize large programs

Reuse code

Improve readability

Reduce complexity

Model real-world entities

3️⃣ Key Concepts of OOP

1️⃣ Class
2️⃣ Object
3️⃣ Encapsulation
4️⃣ Inheritance
5️⃣ Polymorphism
6️⃣ Abstraction

4️⃣ Class

A class is a blueprint for creating objects.

Syntax
class ClassName:
    pass

Example
class Student:
    name = "Pavani"
    age = 20

5️⃣ Object

An object is an instance of a class.

s1 = Student()
print(s1.name)
print(s1.age)

6️⃣ __init__() Constructor

Used to initialize object data.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Pavani", 20)
print(s1.name, s1.age)

7️⃣ self Keyword

Refers to the current object

Used to access class variables

class Demo:
    def show(self):
        print("Hello")

obj = Demo()
obj.show()

8️⃣ Instance Variables vs Class Variables
class Demo:
    x = 10          # class variable
    def __init__(self, y):
        self.y = y  # instance variable

9️⃣ Methods in Class
class Math:
    def add(self, a, b):
        return a + b

m = Math()
print(m.add(10, 20))
