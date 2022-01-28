from collections import Counter
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        adjacents = Counter(nums)
        result = []
        for d in nums:
            if d+1 not in adjacents and d-1 not in adjacents and adjacents[d] == 1:
                result.append(d)
        return result
            
        