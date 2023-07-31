
# example1 creating set
myset = {"apple", "banana", "cherry"}
print(myset)
# example2 : accessing items from set

for i in myset:
    print(i)

# example3: value exists in set or not
print("banana" in myset)
print("banana2" in myset)

# example4: adding items to set
myset.add("orange")
myset.update(["mango", "grapes"])
print(myset)

# example5 : find number of items
print(len(myset))
# example6: remove items
myset.remove("mango")
myset.discard("xsd")
print(myset)
# example 7 : join two sets use union function
myset1 = {1, 2, 3, 7}
myset3 = myset.union(myset1)
print(myset3)


