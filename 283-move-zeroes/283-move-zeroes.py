class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeroIndices = deque()
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         zeroIndices.append(i)
        #     elif zeroIndices:
        #         nums[zeroIndices.popleft()], nums[i] = nums[i], 0     
        #         zeroIndices.append(i)
        #     i += 1
            
            ## smart code without extra space
        lastSeenZeroIndex, n = 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[lastSeenZeroIndex], nums[i] = nums[i], nums[lastSeenZeroIndex]
                lastSeenZeroIndex += 1

            
            
        