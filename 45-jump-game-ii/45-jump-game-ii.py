class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        longestLeap = currentLeapDest = noOfJumps = 0
        for i in range(n-1):
            longestLeap = max(longestLeap, i+nums[i])
            if i == currentLeapDest:
                noOfJumps += 1
                currentLeapDest = longestLeap
        return noOfJumps
        