class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        moneyTillThisHouse = [0]*(n+1)
        moneyTillThisHouse[0] = 0
        moneyTillThisHouse[1] = nums[0]
        for i in range(2,n+1):
            moneyTillThisHouse[i] = max(moneyTillThisHouse[i-1], moneyTillThisHouse[i-2]+nums[i-1])
        return moneyTillThisHouse[n]