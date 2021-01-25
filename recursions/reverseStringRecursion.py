def reverseStringRecursion(string):
  if len(string) == 0:
    return string
  return reverseStringRecursion(string[1:]) + string[0]