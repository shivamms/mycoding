class Solution:
    def __init__(self):
        self.robbed, self.robDP = self.robMaster()
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        self.robDP(nums, 0)
        return max(self.robbed.values())
    
    def robMaster(self):
        robbed = {}
        def robNow(nums, house):
            if house >= len(nums):
                return 0
            elif house in robbed:
                return robbed[house]
            else:
                maxrobbed = max(robNow(nums,house + 1), nums[house] + robNow(nums, house + 2))
                robbed[house] = maxrobbed
                return maxrobbed
        return robbed, robNow
                
    
                