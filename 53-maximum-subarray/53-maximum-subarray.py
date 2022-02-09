class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        print(maxSum, curSum)
        for i in range (1, len(nums)):
            if nums[i] <= curSum + nums[i]:
                curSum += nums[i]
                if maxSum < curSum:
                    maxSum = curSum
                print(maxSum, curSum)
            else:
                if nums[i] > maxSum:
                    maxSum = nums[i]
                curSum = nums[i]
                print(maxSum, curSum)
        return maxSum
                
            