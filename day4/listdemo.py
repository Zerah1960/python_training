
#Example1 : how to create list

mylist1 = [10, 20, 30, 40, 50]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = ["apple", 10, 20]
mylist = list()
print(mylist)
print(mylist1)
print(mylist2)
print(mylist3)
# Example2 : accessing items from the list

mylist = ["apple", "banana", "cherry"]  #index starts from 0
print(mylist[0])
print(mylist[2])
print(mylist[-1])

#range of indexes

mylist = [2, "cherry", 90, "kiwi", "melon", "mango"]
mylist[0] = "orange"
print(mylist)
for i in mylist:
    print(i)

print(mylist.__contains__("Yaourt"))

if "mango" in mylist:
    print("yes l have mango")
else:
    print(" there is not")

print(len(mylist))
mylist.insert(2, "watermelon")
print(mylist)
mylist.remove("mango")
print(mylist)
mylist.pop(4)
print(mylist)
del mylist[0]
print(mylist)
mylist2 = list(mylist)

mylist2 = mylist.copy()
print(mylist)
print(mylist2)

mylist3 = mylist + mylist2
print(mylist3)
mylist.extend(mylist2)
print(mylist)


