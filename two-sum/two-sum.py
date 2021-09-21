from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = defaultdict()
        for i, n in enumerate(nums):
            if (target - n) in track:
                return [track[target - n],i]
            track[n] = i
        