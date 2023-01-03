def sum(v):
    if v==1:
        return 1
    ans = v + sum(v-1)
    return ans
ans=sum(6)
print(ans)



def f1(v):
  if (v <= 1):
    return 1
  return f2(v - 1)

def f2(v):
  if (v <= 2):
    return 2
  
  return f1(v - 1)

ans = f1(3)
print(ans)