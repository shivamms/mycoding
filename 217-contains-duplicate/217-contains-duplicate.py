class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if max(count.values()) > 1:
            return True
        return False
        
        