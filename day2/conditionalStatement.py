# conditional statements
# if if--else elif
# print a person is eligible for vote or not

#  age >=18


age = 15
if age >= 18:
    print("person is eligible for vote")
else:
    print("person is not eligible for vote")


if True:
    print("true condition")
else:
    print("false condition")

num = 24
if num % 2 == 0:
    print("given number is even ")

else:
    print("given number is odd")

a = -10
if a>0:
    print("is a positive number")
elif a<0:
    print("is a negative number")
else:
    print("invalid number")

x = 100
y = 101
if x > y:
    print("x is largest than y")
elif x == y:
    print("x is equal than y")
else:
    print(" y is largest")