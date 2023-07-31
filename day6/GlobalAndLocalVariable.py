# example1

global_var = 20  # global variable


def func():
    local_var = 10  # local variable
    print(local_var)
    print(global_var)


func()

# example2:

xy = 100  # global variable


def cool():
    xy = 200  # local variable
    print(xy)


cool()

# example 3

xy = 100  # global variable


def cool():
    global xy
    xy = 200  # global variable
    print(xy)


cool()
print(xy)

# example4:
x = 100


def cool():
    global x
    x = 500
    print(x)


cool()


# example5

def cool():
    global x
    x = 100
    print(x)


cool()
print(x)
