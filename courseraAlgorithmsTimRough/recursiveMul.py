def recursiveMul(a,b):
  multiplicand = a
  multiplier = reversed(str(b))    
  result = 0
  for i, n in enumerate(multiplier):
    result = result + int(str(add(multiplicand, int(n))) + '0' * i)
  return result

def add(x,n):
  if n == 0:
    return 0
  return add(x,n-1) + x


