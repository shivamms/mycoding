#merge two sorted arrays
#arr1 = [0,3,4,7]
#arr2 = [4,6,8,30,31]
#
#[0,3,4,7,32],[4,6,8,30]
def mergeSortedArrays(arr1, arr2):
  mergedarr = []
  length1 = len(arr1)
  length2 = len(arr2)
  i = 0
  j = 0
  while i < length1 and j < length2:
    if arr1[i] <= arr2[j]:
      mergedarr.append(arr1[i])
      i += 1
    else:
      mergedarr.append(arr2[j]) 
      j += 1
  if i < length1:
    mergedarr.extend(arr1[i:])
  else:
    mergedarr.extend(arr2[j:])
  return(mergedarr)

#using built-in function sorted()
def mergeSortedArraysSmarter(arr1, arr2):
  return sorted(arr1 + arr2)
