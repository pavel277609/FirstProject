from myModule import Person
from myPackage.car import car

def add(a,b):
    result = a+b
    print("result is" + " " + str(result))
    return a+b

def addnumeric(a,b):
    return a+b

def subtract(a,b):
    return a-b

def devide(a,b):
    return a/b


if __name__ == "__main__":
    add(4,5)
    person1 = Person()
    person1.name = "Pavel"
    person1.sayHello()
    mycar = car()
    mycar.name = "santro"
    mycar.sayHello()
    print(":".join("Python"))
    A = [(10, 20, 30, 40, 50), ["Wipro", "Oracle", "Microsoft"]]
    print(type(A[1]))

    if True or False and not False:
        print('T')
    else:
        print('F')
    a = [1, 2, 3, None, (), [], ]
    print(len(a))

    a = None
    x = {}
    print(type(x))

    d = {0: 'a', 1: 'b', 2: 'c'}
    for i in d:
        print(i)

    d = {0: 'a', 1: 'b', 2: 'c'}
    for x in d.keys():
        print(d[x])

    a = [0, 1, 2, 3]
    for a[1] in a:
        print(a[0])
        print(a[1])

    print('Pavel is here to learn')
    print('Changing again')




