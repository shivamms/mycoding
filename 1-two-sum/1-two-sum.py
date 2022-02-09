class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = defaultdict(int)
        for i, num in enumerate(nums):
            if num in comps:
                return i, comps[num]
            comps[target-num] = i
    
            
        
        