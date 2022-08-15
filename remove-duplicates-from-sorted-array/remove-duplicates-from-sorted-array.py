class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastSeenIndex, n = 0, len(nums)
        for i in range(1,n):
            if nums[lastSeenIndex] != nums[i]:
                nums[lastSeenIndex+1] = nums[i]
                lastSeenIndex += 1
        nums = nums[:lastSeenIndex+1]
        return len(nums)