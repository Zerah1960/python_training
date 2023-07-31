# name = "John"
# age = 30
# salary = 5000.50

name, age, salary = "John", 30, 5000.50
# Approach 1
# print(name)
# print(age)
# print(salary)
print(name, age, salary)
# Approach 2
# name is :  John
# age is :  30
# salary is :  5000.5
print("name is : ", name)
print("age is : ", age)
print("salary is : ", salary)

# Approach 3

# print("name is:%s age is:%d salary is:%g" %(name,age,salary))     #s-->string d-->digital g--->decimal
# Approach 4 {}
print("name is:{} age is:{} salary is:{}" .format(name,age,salary))
