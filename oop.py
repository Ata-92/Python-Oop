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

# class attribute ve instance attribute

# Person.name = "Henry"

# print(person1.name)
# print(person2.name)

# person1.name = "Aaron"
# print(person1.name)
# print(person2.name)

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

# Static Methods

class Person:
    name = 'Barry'
    age = 44

    def set_details(self):
        self.name = "Rafe"
        print(self.name)
        self.location = "Turkey"

    @staticmethod
    def salute():
        print("Hi there!", Person.name)

person = Person()
person.set_details()
person.salute()
Person.salute()
