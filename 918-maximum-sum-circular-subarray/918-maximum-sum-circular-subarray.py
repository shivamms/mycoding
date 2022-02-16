class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int: 
        n = len(nums)
        minSum = curMinSum = maxSum = curMaxSum = arraySum = nums[0]
        for i in range(1,n):
            curMaxSum = max(nums[i], curMaxSum+nums[i])
            maxSum = max(curMaxSum, maxSum)
            curMinSum = min(nums[i], curMinSum+nums[i])
            minSum = min(curMinSum, minSum)
            arraySum += nums[i]
        if arraySum == minSum:
            return maxSum
        return max(maxSum, arraySum-minSum)