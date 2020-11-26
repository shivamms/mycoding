import math
#simpler, straightforward
def reverseStringSimple(string):
  reversedstr = ''
  for i in range(len(string)-1,-1,-1):
    reversedstr = reversedstr + string[i]
  return reversedstr

#better, reduce the processing time to half even though the Big O remains same to O(n)
def reverseStringBetter(string):
  mid = math.floor(len(string) / 2)
  mod = len(string) % 2
  if mod == 0:
    reversedstr = ''
    i = mid -1
    j = mid
  else:
    reversedstr = string[mid]
    i = mid - 1
    j = mid + 1
  while i >=0 and j <= len(string) - 1:
    reversedstr = string[j] + reversedstr + string[i]
    i -= 1
    j += 1
  return reversedstr

#smarter way when using built-in feature
def reverseStringSmarter(string):
  return string[::-1]