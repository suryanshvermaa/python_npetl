# List in python
# It can store different type of elements (integer,string,float boolean

marks=[88,90,13,23,56,39,77]
marks[0]=100 # allowed in python

# List slicing
print(marks[:5]) # same as string slicing
# add element
marks.append(0)
print(marks)
# sort the elements
marks.sort()
print(marks)
# reverse sort
marks.sort(reverse=True)
print(marks)
# reverse 
marks.reverse()
# insert at an index
marks.insert(2,88)
print(marks)
