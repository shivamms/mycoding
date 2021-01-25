def fibonacciNonRecursive(index):
  num1 = 0
  num2 = 1
  indexvalue = 0
  for i in range(3,index+1):
    indexvalue = num1 + num2
    num1 = num2
    num2 = indexvalue
  return indexvalue

def fibonacciRecursive(index):
  if index == 1:
    return 0
  elif 2 >= index <= 3:
    return 1
  return fibonacciRecursive(index - 1) + fibonacciRecursive(index - 2)