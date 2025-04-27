# count number of "A" in the list
def countA(list):
    count=0
    for i in range(0,len(list)):
        if list[i]=="A":
            count+=1
    return count

arr=input("Enter list of characters:").split(" ")
print(countA(arr))