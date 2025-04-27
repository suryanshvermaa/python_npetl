# while loop
# prints numbers from 1 to 100
# i=1
# while i<=100:
#     print(i,end=" ")
#     i+=1
# print()

# print list elements using for loop
list=[3,2,4,3,5,7,9,10,44,55]
for i in range(0,len(list)):
    print(list[i],end=" ")
print()

# break and continue
for i in range(0,len(list)):
    if i==5:
        continue
    print(list[i],end=" ")
    if i==10:
        break
print()

for el in list:
    print(el,end=" ")
print()

# pass statement -> pass is a null statement that does nothing. It is used as a placeholder for future code

for i in range(10):
    pass