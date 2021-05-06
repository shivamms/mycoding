class Solution:
    from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0,0
        hashtable = defaultdict(int)
        hashtable[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if hashtable[sum-k]:
                count += hashtable[sum-k]
            hashtable[sum] += 1
        return count