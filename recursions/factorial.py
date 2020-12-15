#recursive - structure
#base case
#recursive case
#return base case and recursive case
def factorialNonRecursive(num):
  fac = 1
  for i in range(2,num+1):
    fac = fac * i
  return fac


def factorialRecursive(num):
  #base case
  if num == 1:
    #return base case
    return num
  #recursive case and return recursive case 
  return num * factorialRecursive(num - 1)

