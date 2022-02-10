class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                right = pivot -1
                if left > right:
                    return pivot
            else:
                if left == right:
                    return pivot + 1
                left = pivot + 1