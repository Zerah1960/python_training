# example1: when you write a function into a class it calls method
#
# class MyClass:
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print(name)
#
#
# mc1 = MyClass()
# mc1.myfun()
# mc1.display("Scott")

# example2:
# class MyClass:
#     def m1(self):
#         print("this is instance method...")
#
#     @staticmethod
#     def m2(self, num):
#         print(self, num)
#
#
# mc = MyClass()
# mc.m1()
# mc.m2(100, 200)
#
# MyClass.m2(100, 200)

# instance method ( we can call only through object)
# static method (we can directly call using class)

# example3:
# class MyClass:
#     a, b = 10, 20  # class variables
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mult(self):
#         print(self.a * self.b)
#
#
# mc = MyClass()
# mc.add()
# mc.mul()

# example3:
# i, j = 15, 25  # global variable


# class MyClass:
#     a, b = 10, 20
#
#     def add(self, x, y):
#         print(x + y)  # x, y local variables
#         print(self.a + self.b)  # a, b are class variables
#         print(i + j)  # i, j are global variable
#
#
# mc = MyClass()
# mc.add(100, 200)
#
# a, b = 15, 25  # global variables
#
#
# class MyClass:
#     a, b = 10, 20
#
#     def add(self, a, b):
#         print(a+b)  # a, b local variables
#         print(self.a + self.b)  # a, b are class variables
#         print(globals()["a"]+globals()["b"])  # a, b are global variable
# mc = MyClass()
# mc.add(100,200)

# example6: constructor example

class MyClass:
    def __init__(self):
        print(" this is constructor....")

    def m1(self):
        print("hello world!!")

    def m2(self, x, y):
        return (x + y)


#
# mc = MyClass()  # invoke constructor automatically
# mc.m1()  # method we have call explicitly by using object
# print(mc.m2(10, 20))

class MyClass:
    name = "John"

    def __init__(self, name):
        print(name)
        print(self.name)


mc = MyClass("Zokora")


# example9
# requirement : employees
# constructor : eid, ename and salary
# display() : print eid, ename, sal

class Emp:
    # eid = ""
    # ename = ""
    # sal = ""
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return(self.ename)


e1 = Emp(101, "John", 500000)
print(e1)

