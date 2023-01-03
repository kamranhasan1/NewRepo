import math

def findfactorial(v):
    fact=1
    for i in range (1,v+1):
        fact=fact*i
    return fact
print(findfactorial(3))

#blackbox definition
def multiply(a, b):
    sum=a*b
    return sum
ans=multiply(4,5)
print(ans)

def divide(a,b):
     sum=a/b
     return sum
ans= divide(4,2)
print(ans)

def sum (a,b):
    sum=(a*b)
    return sum
a=int(input())
b=int(input())
d=sum(a,b)
print('a/bxc=',d)

