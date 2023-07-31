a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
list = [10, 20, 30, 40, 50]

try:
    if b == 0:
        raise ZeroDivisionError
    c = a / b
    print(list[5])
except ZeroDivisionError:
    print("Divided by Zero exception")
# except IndexError:
#     print("Index is out of Range")
# except:
#     print("Exception raised")
