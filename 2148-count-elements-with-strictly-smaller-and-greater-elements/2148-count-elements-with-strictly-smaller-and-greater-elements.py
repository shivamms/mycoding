from collections import defaultdict
class Solution:
    def countElements(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        sindex, bindex = 0, 0
        smaller, bigger = [0]*n, [0]*n
        eligible = set()
        for i in range(n):
            if nums[sindex] < nums[i] < nums[bindex]:
                smaller[i] += 1
                bigger[i] += 1
            elif nums[sindex] < nums[i] > nums[bindex]:
                bigger[bindex] += 1
                bindex = i
                smaller[i] += 1
            elif nums[sindex] > nums[i] < nums[bindex]:
                smaller[sindex] += 1
                sindex = i
                bigger[i] += 1
            elif nums[sindex] < nums[i] == nums[bindex]:
                smaller[i] += 1
            elif nums[sindex] == nums[i] < nums[bindex]:
                bigger[i] += 1
        for i in range(n):
            if smaller[i] > 0 and bigger[i] > 0 or nums[i] in eligible:
                eligible.add(nums[i])
                result += 1
        return result
        
            
                
            
        