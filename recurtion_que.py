def convertToBaseN(val, N):
  if(val < N):
    return str(val)
  
  currDigit = str(val % N)
  return convertToBaseN(val//N, N) + currDigit

ans = convertToBaseN(6,2)
print(ans)


