class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = dict()
        for i, num in enumerate(nums):
            if num in comp:
                return [comp[num], i]
            else:
                comp[target-num] = i
        