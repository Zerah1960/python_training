# example 1: creating dictionary
mydic = {
    "brand": "hyndai",
    "model": "i30",
    "year": 2021
}
# print(mydic["brand"])

print(mydic.get("brand"))

# example2: change value in dictionary

mydic = {
    "brand": "hyndai",
    "model": "i30",
    "year": 2021
}
mydic["year"] = 2022
print(mydic)
# example5: reading items from dictionary using loop

for i in mydic:
    print(i)  # print only key from dictionary

for i in mydic:
    print(mydic[i]) # print only values from dictionary

for i in mydic.values():
    print(i)   # print only values from dictionary

for i in mydic.keys():
    print(i)


for x,y in mydic.items():
    print(x,y)   # print keys along with values from dictionary

# example6: key exist in dictionary or not

mydic = {
    "brand": "hyndai",
    "model": "i30",
    "year": 2021
}

if "model" in mydic:
    print("exist")
else:
    print("not exist")

print(len(mydic))

# example7: add items
mydic["color"]= "red"    # add new items to dictionary
print(mydic)

# example8: remove items from dictionary
mydic.pop("brand")
print(mydic)
# mydic= mydic2
mydic2= mydic.copy()
print(mydic2)

def cool():
    global x
    x = 100
    print(x)
cool()