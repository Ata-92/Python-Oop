# def printtype(data):
#     for i in data:
#         print(i, type(i))

# testdata = [123, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x, {'name':'Barry'}]
# printtype(testdata)

# class Person:
#     name = 'Barry'
#     age = 44

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# --------------------------
# class attribute ve instance attribute

# Person.name = "Henry"

# print(person1.name)
# print(person2.name)

# person1.name = "Aaron"
# print(person1.name)
# print(person2.name)

# --------------------------
# SELF keyword

# class Person:
#     name = "Barry"
#     age = 44

#     def test(self):
#         pass

#     def get_details(self):
#         print("Name:", self.name, "Age:", self.age, "Location:", self.location)

#     def set_details(self):
#         self.name = "Rafe"
#         print(self.name)

#         self.location = "Turkey"
#         print(self.location)

# person = Person()
# person.test()
# Person.test(person)

# person.set_details()
# person.get_details()
# print(person.location)
# print(Person.location)
# print(Person.name)

# --------------------------
# Static Methods

# class Person:
#     name = 'Barry'
#     age = 44

#     def set_details(self):
#         self.name = "Rafe"
#         print(self.name)
#         self.location = "Turkey"

#     @staticmethod
#     def salute():
#         print("Hi there!", Person.name)

# person = Person()
# person.set_details()
# person.salute()
# Person.salute()

# --------------------------
# Special methods

# class Person:
#     company = "Clarusway"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name} Age: {self.age}"

#     def __len__(self):
#         return self.age

# person = Person("Barry", 44)
# print(person.name)

# lst = [1,2,3]
# print(lst)
# print(person)
# print(person.__str__())

# print(len(lst))
# print(len(person))
# print(person.__len__())

# --------------------------
# encapsulation and abstraction

# class Person:
#     company = 'Clarusway'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id1 = 2002
#         self.__id2 = 5005

#     def __str__(self):
#         return f'Name : {self.name} Age: {self.age}'

# person = Person("Rafe", 39)
# person._id1 = 3003
# print(person._id1)
# person.__id2 = 4004
# print(person.__id2)
# print(person._Person__id2)

# ----------------------------
# inheritance and polymorphism

# class Person:
#     company = "Clarusway"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name} Age: {self.age}"

#     def details(self):
#         print(f"Company: {Person.company}\nName: {self.name}\nAge: {self.age}")

# class Lang:
#     def __init__(self):
#         pass

# class Employee(Person, Lang):  # multiple inheritance
#     def __init__(self, name, age, path):
#         # self.name = name
#         # self.age = age
#         super().__init__(name, age)
#         Lang.__init__(self)
#         self.path = path

#     # override

#     def details(self):
#         print(f"Company: {Person.company}\nName: {self.name}\nAge :{self.age}\nPath: {self.path}")

# emp = Employee("Barry", 44, "FullStack")
# emp.details()
# print(Employee.mro())

# ----------------------
# getter and setter

# class Person:
#     company = 'Clarusway'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__salary = 5000

#     def __str__(self):
#         return f'Name : {self.name} Age: {self.age}'

#     def details(self):
#         print(f'Company: {Person.company}\nName: {self.name}\nAge :{self.age}')

#     @property
#     def salary(self):
#         print("getter called")
#         return self.__salary

#     @salary.setter
#     def salary(self, salary):
#         # if salary < 2000 or salary > 10000:
#         if not 2000 < salary < 10000:
#             raise ValueError('Invalid salary.')
#         print('setter called')
#         self.__salary = salary

# person = Person("Barry", 44)
# person.salary = 1000
# print(person.salary)

# -------------------------
# inner class

# from django.db import models

# class Article(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

#     # inner class
#     class Meta:
#         ordering = ["last_name"]
#         abstract = True

# -----------------------
# overloading an operator

class Square:
    def __init__(self, side):
        self.side = side
        self.premiter = self.side * 4

    def __add__(x, y):
        return x.premiter + y.premiter

x = 2
y = 5

a = "Barry"
b = "Mitchell"

print(x + y)
print(a + b)

sqr1 = Square(5)
sqr2 = Square(4)

print('Total premiter is ', sqr1 + sqr2)
