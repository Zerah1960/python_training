# example 1
# def func(i, j):
#    print(i,j)
#
#
# # func(10, 20)  # Positional arguments
# func(j=20, i=10)  # keyword arguments
# example 2

def func(i, j=10):
    print(i, j)


func(100, 200)


# example3 keyword arguments

def greeting(name, greetmsg):
    print(greetmsg + "  " + name)


greeting(name="John", greetmsg="hello ")
greeting(greetmsg="hello", name="John")


# example4

def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)  # positional arguments
my_func(a=10, b=20, c=30)  # keyword arguments
my_func(b=20, a=10, c=30)  # keyword arguments


# my_func(b=20, a=10,30)  # This is wrong as positional argument must occur before any keyword argument
#  example 5

def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(100, 200))
