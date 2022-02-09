from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for number in nums:
            count[number] += 1
            if count[number] > 1:
                return True
        return False
        