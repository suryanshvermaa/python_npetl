# WAF to find factorial of a number
def fact(n):
    if (n==0 or n==1) : return 1
    else: return n*fact(n-1)

print(fact(3))
print(fact(4))
print(fact(5))