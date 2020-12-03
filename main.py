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
import arrays.longestWord as lw

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

print(lw.LongestWord("fun&!!  time  "))
print(lw.LongestWord("I love dogs"))
print(lw.LongestWord("this is some sort of sentence"))


