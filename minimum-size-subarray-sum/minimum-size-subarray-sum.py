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

# target = 7
# nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]
# target = 11
# nums = [1,1,1,1,1,1,1,1]
# target = 80
# nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
# target = 15
# nums = [1,2,3,4,5]
# print(minSubArrayLen(target, nums))           
            
            