# def printtype(data):
#     for i in data:
#         print(i, type(i))

# testdata = [123, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x, {'name':'Barry'}]
# printtype(testdata)

class Person:
    name = 'Barry'
    age = 44

person1 = Person()
person2 = Person()

print(person1.name)
print(person2.name)

# class attribute ve instance attribute

Person.name = "Henry"

print(person1.name)
print(person2.name)

person1.name = "Aaron"
print(person1.name)
print(person2.name)
