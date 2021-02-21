class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        numlen,sum, start, end  =  len(nums), 0, 0, -1
        minlength = numlen + 1
        while end < numlen - 1:
            end += 1
            sum += nums[end]
            while sum >= target:
                minlength = min(minlength, end - start + 1)
                sum -= nums[start]
                start += 1
            if minlength == 1: 
                return 1  
        return minlength if minlength < numlen + 1 else 0
            
            
            
            