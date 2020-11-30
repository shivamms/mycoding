#import comparelists as cl
#import haspair as hp
#import arrays.implementArray as array
#import arrays.reverseString as rs
#import arrays.mergeSortedArrays as msa
import arrays.maxSubArray as msub

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
print(msub.maxSubArray([3,-1,4,5,2,7]))
