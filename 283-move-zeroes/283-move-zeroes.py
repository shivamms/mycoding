class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndices = deque()
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroIndices.append(i)
            elif zeroIndices:
                nums[zeroIndices.popleft()], nums[i] = nums[i], 0     
                zeroIndices.append(i)
            i += 1
            
        