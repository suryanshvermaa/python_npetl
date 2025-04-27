# WAP to check list contains all palindrome numbers or not
def isPalindrome(str):
    i=0
    j=len(str)-1
    while i<j:
        if str[i]!=str[j]:
            return False
        i+=1
        j-=1
    return True

arr=input("Enter list of strings:").split(" ")
flag=True
for i in range(0,len(arr)):
    if not isPalindrome(arr[i]):
        flag=False
        break
if flag==True:
    print("This is a Palindrom list")
else:
    print("This is not a Palindrom list")

