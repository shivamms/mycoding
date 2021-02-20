def mergesort(arr: list) -> list:
  length = len(arr)
  if length <= 1:
    return arr
  mid = length // 2
  left = mergesort(arr[:mid])
  right = mergesort(arr[mid:])
  if left is not None and right is not None:
    temp =  merge(left, right)
    return temp


def merge(left, right):
  sortedarray = []
  llength = len(left)
  rlength = len(right)
  while len(left) > 0 and len(right) > 0:
    if left[0] > right[0]:
      sortedarray.append(right[0])
      right = right[1:]
    else:
      sortedarray.append(left[0])
      left = left[1:]

  while len(left) > 0:
      sortedarray.append(left[0])
      left =left[1:]
   
  while len(right) > 0:
    sortedarray.append(right[0])
    right = right[1:]
  return sortedarray


    

