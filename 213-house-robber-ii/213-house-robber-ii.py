class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robFrom(houses):
            n = len(houses)
            moneyTillThisHouse = [0]*(n+1)
            moneyTillThisHouse[0] = 0
            moneyTillThisHouse[1] = houses[0]
            for i in range(2,n+1):
                moneyTillThisHouse[i] = max(moneyTillThisHouse[i-1], moneyTillThisHouse[i-2]+houses[i-1])
            return moneyTillThisHouse[n]
        
        return max(robFrom(nums[:-1]), robFrom(nums[1:]))