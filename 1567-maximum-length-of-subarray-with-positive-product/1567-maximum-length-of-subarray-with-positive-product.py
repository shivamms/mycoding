class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # neg: Length of longest negative-product subarray ending with nums[i]
        # pos: Length of longest positive-product subarray ending with nums[i]
        ans = pos = neg = 0
        for i in range(n):
            if nums[i] > 0:
                pos, neg = pos+1, neg+1 if neg else 0
            elif nums[i] < 0:
                pos, neg = neg+1 if neg else 0, pos+1
            else:
                pos = neg = 0
            ans = max(ans, pos)
        return ans
        