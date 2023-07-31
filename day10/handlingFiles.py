
# example1: writing data in to text file

# file = open("/Users/laurentzerahmpakondema/LINUX_COMMANDS/file1.txt","w")
# file.write("This is my first statement.....\n")
# file.write("This is my second statement....\n")
# file.write("This is my third statement.....\n")
# file.write("This is my fourth statement....\n")
# file.write("This is my fifth statement....\n")
# file.close()
# print("program completed !!!")

# example2: ready data from text file
# file = open("/Users/laurentzerahmpakondema/LINUX_COMMANDS/file1.txt", "r")
# print(file.read())
# file.close()
# example3: appending data into text file
file = open("/Users/laurentzerahmpakondema/LINUX_COMMANDS/file1.txt", "a")
file.write("This is my sixth line\n")
file.write("This is my seventh line\n")
file.close()
print("Program is completed !!!")