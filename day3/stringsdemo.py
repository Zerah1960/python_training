# s = "welcome"
# name = ""

# mutable can change the value of the variable,
# immutable - cannot change the value of variable
# string are immutable
# if the value is changed after updation then is mutable
str1 = "welcome"
str2 = " to python"
print(id(str1))
print(str1 + str2)
print(str1[:6])
print(str1.endswith("come"))
print(str1.startswith("come"))
print(str1.upper())
# print(str1.replace("welcome","Bonjour"))
rev_str1 = str1[::-1]
print(rev_str1)
