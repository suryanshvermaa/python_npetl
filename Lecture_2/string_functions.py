# String functions
str="i am a student of NIT Patna"
print(str.endswith("Patna")) # returns true if string ends with this substr
print(str.endswith("am"))
print(str.startswith("i"))

print(str.capitalize()) # capitalise first character and small all other characters
print(str.replace("Patna","Bihta"))
print(str.find("Patna")) # returns the index of first character
print(str.count("a")) # count the occurance of substring