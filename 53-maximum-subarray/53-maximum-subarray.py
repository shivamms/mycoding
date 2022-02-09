class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        for i in range (1, len(nums)):
            if nums[i] <= curSum + nums[i]:
                curSum += nums[i]
            else:
                curSum = nums[i]
            if maxSum < curSum:
                maxSum = curSum

        return maxSum
                
            