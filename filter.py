def evenFilter(v):
    if(v%2==0):
        return True
    return False
l=[12,3,4,5,8,9,6,12]
even=list(filter(evenFilter,l))
print(even)

import math
def gcd(a,b):
    g=(math.gcd(a,b))
    print(g)

    gcd(12,14)
