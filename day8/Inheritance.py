# example1:

# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()

# aobj = A()
# aobj.m1()

# example2:

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 100, 200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()


# example3: multilevel inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# example4:  hierarchy inheritance
#
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)


# bobj = B()
# bobj.m1()
# bobj.m2()
#
#
# cobj = C()
# cobj.m1()
# cobj.m3()

# example 5: multiple inheritance


# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B:
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A,B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# example6:
#
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1()
#
#
# bobj = B()
# bobj.m1()

# example7:

# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#
#     def m(self, x, y):
#         print(x + y)
#         print(self.i + self.j)
#         print(self.a + self.b)
#
# bobj = B()
# bobj.m(1000,2000)


# example8: overriding variables

# class Parent:
#     name = "Scott"


# class Child(Parent):
#     name = "John"
#
#     def test(self):
#         print(super().name)
#
#
# cobj = Child()
# print(cobj.name)
# cobj.test()

# example9: Overriding methods

# class Bank:
#     def rateOfInterest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
#
#
# objx = XBank()
# print(objx.rateOfInterest())
#
# objy = YBank()
# print(objy.rateOfInterest())


# example10: Overloading polymorphism


class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")

h = Human()
h.sayHello("John")
h.sayHello()


# example11:Overloading2
#
# class Calculation:
#     def add(self, a=0, b=0, c=0):
#         print(a+b+c)
#
# calobj=Calculation()
# calobj.add()
# calobj.add(10, 20)
# calobj.add(100, 200, 300)