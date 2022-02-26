class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, localSum = nums[0], nums[0]
        for i in range(1,len(nums)):
            localSum = max(localSum+nums[i], nums[i])
            maxSum = max(localSum, maxSum)
        return maxSum
                
        