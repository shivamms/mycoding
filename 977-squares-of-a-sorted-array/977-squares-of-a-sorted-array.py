class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minimumNum = math.inf
        for i, num in enumerate(nums):
            if abs(num) < minimumNum:
                minimumNum = abs(num)
                minimumNumIndex = i
        result = [minimumNum**2]
        i = minimumNumIndex-1
        j = minimumNumIndex+1
        n = len(nums)
        while i >= 0 or j < n:
            leftSqr = nums[i]**2 if i >= 0 else math.inf
            rightSqr = nums[j]**2 if j < n else math.inf
            if leftSqr < rightSqr: 
                result.append(leftSqr)
                i -= 1
            else:
                result.append(rightSqr)
                j += 1
        return result
            
        