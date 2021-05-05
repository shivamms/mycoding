class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        p = [1] * length
        p[0] = 1
        for i in range(1,length):
            p[i] = p[i-1] * nums[i-1]
        rightp = 1
        for i in reversed(range(length)):
            p[i] *= rightp
            rightp *= nums[i]
        return p
        