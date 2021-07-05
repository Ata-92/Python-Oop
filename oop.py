def printtype(data):
    for i in data:
        print(i, type(i))

testdata = [123, 'Barry', [1,2,3], (1,2,3), {1,2,3}, True, lambda x: x, {'name':'Barry'}]
printtype(testdata)

class Person:
    name = 'Barry'
    age = 44
