class Solution:
    def arraySign(self, nums: List[int]) -> int:
        numOfNeg = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                numOfNeg += 1
        return 1 if numOfNeg % 2 == 0 else -1