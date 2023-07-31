# example1

# print("This is starting point of program...")
# print("This is starting point of program...")
# print("This is starting point of program...")
# try:
#     print(x)
# except:
#     print("Exception occurred")
#
# print("this is end of the program..")
# print("this is end of the program..")
# print("this is end of the program..")

# example2
# print("This is starting point of program...")
# print("Program in progress")
# try:
#     print(10 / -0)
# except:
#     print("Exception occurred.. handled")
# print("Program completed let's continue !!!")

# example3: Multiple except blocks - try, except else, finally
# try:
#     num1, num2 = 10, 0
#     result = num1 / num2
#     print("result is ", result)
# except ZeroDivisionError:
#     print("Thrown error ZeroDivisionError")
# except SyntaxError:
#     print("Thrown Syntax error exception")
# except:
#     print("Exception handled")
# else:
#     print("No exception occurred")
# finally:
#     print("Always execute...")

# example4: raising our own exceptions

def EnterAge(num):
    if num < 0:
        raise ValueError("Only Integers are allowed")
    elif num % 2 == 0:
        print(" number is even number")
    else:
        print(" number is odd number")


num = -1
try:
    EnterAge(num)
except ValueError:
    print("Value error exception occurred and handled...")

EnterAge(-1)
