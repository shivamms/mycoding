class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N) solution with DP
        # maxSum = curSum = nums[0]
        # for num in nums[1:]:
        #     curSum = max(num, curSum + num)
        #     maxSum = max(curSum, maxSum)
        # return maxSum
        
        # divide and conquer
        def dcMaxSubarray(nums, left, right):
            if left > right:
                return -math.inf
            mid = (left + right) // 2
            currSum = maxLeftSum = maxRightSum = 0
            
            for i in range(mid-1, left-1, -1):
                currSum += nums[i]
                maxLeftSum = max(maxLeftSum, currSum)
            
            currSum = 0
            for i in range(mid+1, right+1):
                currSum += nums[i]
                maxRightSum = max(maxRightSum, currSum)
            
            maxSum = maxLeftSum + nums[mid] + maxRightSum
            
            leftSum = dcMaxSubarray(nums, left, mid-1)
            rightSum = dcMaxSubarray(nums, mid+1, right)
            
            return max(maxSum, leftSum, rightSum)
            
        return dcMaxSubarray(nums, 0, len(nums) - 1)
                
            