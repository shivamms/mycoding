class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        lastNonZero = 0
        while i<n:
            if nums[i] != 0:
                nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
                lastNonZero += 1
            i += 1
#         zero = deque()
#         pos = None
#         n = len(nums)
#         i = 0
#         while i<n:
#             if nums[i] != 0:
#                 pos = i
#                 if zero and zero[0] < pos:
#                     nums[zero[0]], nums[pos] = nums[pos], nums[zero[0]]
#                     zero.popleft()
#                     zero.append(i)
#                     pos = None
#             else:
#                 zero.append(i)
#                 if pos and pos > zero[0]:
#                     nums[zero[0]], nums[pos] = nums[pos], nums[zero[0]]
#                     zero.popleft()
#                     zero.append(i)
#                     pos = None 
#             i += 1

                