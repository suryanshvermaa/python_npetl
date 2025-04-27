# # open, read & close file
# # write file
f=open("file.txt","w")
f.write("Hi this is sample file!!!")
f.close()

# reading file
f=open("file.txt","r")
data=f.read() # read all file
print(data)

# # append content in file
# f=open("file.txt","a")
# f.write("\n Hello npetl")

# appending data "with Syntax"
with open("file.txt","r") as f:
    data=f.read()
print(data)

# deleting the file
# import os
# os.remove("file.txt")