#Given a collection of numbers, check if they have a pair which is equal to a given sum
#Numbers are in list
#Numbers of negative/positive integers arranged in ascending order
#There can be repeated numbers
#There can be empty list

# simple solution
def haspairsumsimple(lst, sum):
  count = 0
  if len(lst) > 0:
    for i in range(len(lst)):
      for j in range(i+1,len(lst)):
        count += 1
        if j < len(lst) and lst[i] + lst[j] == sum:
          print(count)
          return True
  print(count)
  return False

#print(haspairsumsimple([1,2,4,5,9,11,20], 8))

#better solution
#take advantage of ordered list
#check if the first element is <= sum/2
#check if the last element is <= sum/2
#start with first and last element and add them
#if the sum is too big, keep first element and move to one element before the last element
#if the sum is too small, move to second element and keep last element
#repeat untill find the pair

def haspairsumbetter(lst, sum):
  if len(lst) <=0 or lst[0] > sum/2:
    return False
  i = 0
  j = len(lst)-1
  while i < j and i >=0:
    pairsum = lst[i]+lst[j]
    if pairsum == sum:
      return True
    elif pairsum > sum:
      j -= 1
    else:
      i += 1
  return False

#print(haspairsumbetter([1,2,3,6,7], 8))

#what if the list is not ordered
#Create a hashtable with number in the number index as key and the number as Value
#Iterate through the each number in the list and check if the number as well as the sum-number are both in the hash
#To avoid the wrong pair detection in the case of the number being exact half of the sum, remove the number from the hash and check again if the sum-number is in the values of hash

def haspairsumhash1(lst,sum):
  hash = {i: lst[i] for i in range(len(lst))}
  for i in range(len(lst)):
    if sum-lst[i] in hash.values() and lst[i] in hash.values():
      del hash[i]
      if sum-lst[i] in hash.values():
        return True
  return False

#print(haspairsumhash1([5,10,7,4,2,8,0],8))

#another version of hashtable
def haspairsumhash2(lst,sum):
  hash = {}
  for i in range(len(lst)):
    comp = sum-lst[i]
    if comp in hash.values():
      return True
    else:
        hash[i] = comp
  if lst[i-1] == comp:
    return True
  else:
    return False

#print(haspairsumhash2([5,10,7,4,2,8,0],8))
#print(haspairsumhash2([5,10,4,4],8))