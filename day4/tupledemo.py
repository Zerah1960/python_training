
# creating tuple

mytuple = ("apple", "banana", "cherry", "orange")
mytyple1 = ()
print(mytuple)
print(mytuple[-1])
for i in mytuple:
    print(i)

mylist = list(mytuple)
mylist[0]="Orange"
mytuple = tuple(mylist)
print(mytuple)

