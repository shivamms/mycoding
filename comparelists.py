#compare two lists and return true if they have common elements else False

def comparelists(lst1, lst2):
  dic1 = {lst1[i]:'true' for i in range(len(lst1))}
  for i in range(len(lst2)):
    if lst2[i] in dic1.keys():
      return True
  return False

#print(comparelists([1,None,5,'a'], ['f',None,5]))