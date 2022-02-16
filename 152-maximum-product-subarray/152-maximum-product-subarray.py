class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxProd = curMaxProd = curMinProd = nums[0]
        for i in range(1,n):
            temp_max = max(nums[i], curMaxProd*nums[i], curMinProd*nums[i])
            curMinProd = min(nums[i], curMaxProd*nums[i], curMinProd*nums[i])
            curMaxProd = temp_max
            maxProd = max(maxProd, curMaxProd)
        return maxProd