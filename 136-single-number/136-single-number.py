class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for n in nums:
            sum ^= n
        return sum
        