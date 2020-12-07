#import comparelists as cl
#import haspair as hp
#import arrays.implementArray as array
#import arrays.reverseString as rs
#import arrays.mergeSortedArrays as msa
#import arrays.maxSubArray as msub
#import arrays.moveZeroes as mz
#import arrays.containsDuplicate as cd
#import arrays.reverseArray as ra
#import arrays.rotateArray as rta
#import arrays.longestWord as lw
#import hashtable.implementHashTable as iht
#import hashtable.firstRecurring as htfr
import linkedlists.implementLinkedList as ill

#print(cl.comparelists([1,'a'], ['f',None,5]))
#print(hp.haspairsumhash2([5,10,7,4,2,8,0],8))
#print(array.createarray())
#print(rs.reverseStringSimple('subramanian'))
#print(rs.reverseStringBetter('subramanian'))
#print(rs.reverseStringSmarter('subramanian'))
#print(msa.mergeSortedArrays([0,4,6,8,31],[3,7,8,33,40,44]))
#print(msa.mergeSortedArraysSmarter([4,4,4,4,4],[4,4,4,4]))

#print(msub.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#print(msub.maxSubArray([2,4,-3,4,-1,2,1,-5,4]))
#print(msub.maxSubArray([-2,-4,-3,4,-1,-2,-1,-5,-4]))
#print(msub.maxSubArray([-2,4,-3,4,-1,-2,-1,-5,-4]))
#print(msub.maxSubArray([-2,-4,-3,-4,-1,-2,-1,-5,-4]))
#print(msub.maxSubArray([1]))
#print(msub.maxSubArray([-2,-1]))
#print(msub.maxSubArray([-1,3,4,-5,9,-2]))
#print(msub.maxSubArray([3,-1,4,5,2,7]))

#print(mz.moveZeroes([0,1,0,3,12]))
#print(mz.moveZeroes([0,0,0,0,0]))
#print(mz.moveZeroes([1,1,1,1,1,1,1]))
#print(mz.moveZeroes([1,0,0,0,0,4,0,6]))

#print(cd.containsDuplicate([1,2,3,1]))
#print(cd.containsDuplicate([1,2,3,4]))
#print(cd.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

#print(ra.reverseArray([1,2,3,4,5,6,7,8]))
#print(ra.reverseArray([1,2,3,4,5,6,7]))
#print(ra.reverseArray([1]))
#print(ra.reverseArray([]))

#print(rta.rotateArrayRight([4,10,12,8,9,18,0,2,11,23,7,13], 3))
#print(rta.rotateArrayLeft([4,10,12,8,9,18,0,2,11,23,7,13], 3))
#print(rta.rotateArrayRight([4,10,12,8,9,18,0,2,11,23,7,13], -3))
#print(rta.rotateArrayLeft([4,10,12,8,9,18,0,2,11,23,7,13], -3))
#print(rta.rotateArrayRight([4,10,12,8,9,18,0,2,11,23,7,13], 13))
#print(rta.rotateArrayLeft([4,10,12,8,9,18,0,2,11,23,7,13], 13))

#print(lw.LongestWord("fun&!!  time  "))
#print(lw.LongestWord("I love dogs"))
#print(lw.LongestWord("this is some sort of sentence"))

#mydic = iht.hashTable('apple',10000)
#mydic.setValue('orange',2034)
#print(mydic.getValue('apple'))
#print(mydic.getValue('orange'))
#mydic.setValue('1',2)
#print(mydic.getValue('1'))

#print(htfr.firstRecurring([1,2,2,2,2,2,2,3,3,2,3]))
#print(htfr.firstRecurring([1,2,3,4,5,6,7,8,9,10,11]))
#print(htfr.firstRecurring([]))

mynode = ill.node(14)
nextnode = ill.node(18)
mynode.next = nextnode
thirdnode = ill.node(20)
nextnode.next = thirdnode

node = mynode
while 1:
  print(node.value)
  if node.next is None:
    break
  node = node.next

node0 = ill.node("a")
node1 = ill.node("amma")
node2 = ill.node("aadu")
node3 = ill.node("elai")
mylist = ill.linkedlist(node1)
mylist.append(node2)
mylist.append(node3)
mylist.prepend(node0)

mylist.display()

node0.value = "amma"
node1.value = "aadu"
node2.value = "elai"
node3.value = "eli"
node4 = ill.node("Iaindu")
mylist.append(node4)

mylist.display()

node22 = ill.node("eee")
node33 = ill.node("aeni")

mylist.insertafter(node2,node22)
mylist.display()

mylist.insertbefore(node4,node33)
mylist.display()







