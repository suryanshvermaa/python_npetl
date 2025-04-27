# 1- Create a new file "practice.txt" using python. Add the following data in it
"""
Hi Everyone
we are learning File I/O
using Java
I like programming in Java
"""
# 2- WAP that replace all occurances of "Java" with "Python"
# 3- Search if the word "learning" exists in the file or not

# 1
with open("practice.txt","w") as f:
    f.write("""Hi Everyone
we are learning File I/O
using Java
I like programming in Java""")

# 2
with open("practice.txt","r") as f:
    data=f.read()
    data=data.replace("Java","Python")
with open("practice.txt","w") as f:
    f.write(data)

# 3
with open("practice.txt","r") as f:
    data=f.read()
    if "learning" in data:
        print("Yes exists")
    else:
        print("Not exists")

